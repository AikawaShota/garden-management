import datetime
from . import forms
from . import mixins
from .models import Plant, RelatedURL
from .functions import get_watering_state
from utilities.mixins import OwnerOnlyMixin
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


# 植物一覧（水やり状態）
class PlantListView(LoginRequiredMixin, generic.ListView):
    model = Plant
    template_name = "plant_management/plant_list.html"
    context_object_name = "plants"

    # 取得するデータをカスタマイズする。
    def get_queryset(self):
        # .filter()：ユーザが作成したオブジェクトのみ取り出す。
        # .order_by()：priorityの値で降順ソートした後、plant_idで昇順ソートする。
        queryset = self.model.objects \
            .select_related("image") \
            .values("plant_id", "name", "description",
                    "image__path", "image__alt", "last_watering_date",
                    "watering_frequency", "priority") \
            .filter(user=self.request.user) \
            .order_by("-priority", "plant_id")
        return queryset

    # 水やりの状態（水やりの要否・次回の水やりまでの時間）を保存するcontextを追加する。
    def get_context_data(self, **kwargs):
        # 継承元（ListView）のget_context_dataを呼んで、contextを取得。
        context = super().get_context_data(**kwargs)
        plants = context["plants"]
        for plant in plants:
            plant["watering_state"] = get_watering_state(
                plant["last_watering_date"], plant["watering_frequency"]
            )
        context["plants"] = plants
        return context


# 水やり完了処理
def complete_watering(request, pk):
    plant = Plant.objects.get(pk=pk)
    if plant.user != request.user:
        try:
            raise PermissionDenied()
        except PermissionDenied:
            print("You do not have permission to edit.")
            return redirect("authentication:login")
    plant.last_watering_date = datetime.datetime.now()
    plant.save()
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        data = {
            "watering-state": get_watering_state(
                plant.last_watering_date, plant.watering_frequency
            )
        }
    return JsonResponse(data)


# 植物詳細
class PlantDetailView(
    OwnerOnlyMixin, LoginRequiredMixin, generic.DetailView
):
    model = Plant
    template_name = "plant_management/plant_detail.html"
    context_object_name = "plant_detail"

    # 水やりの状態（水やりの要否・次回の水やりまでの時間）を保存するcontextを追加する。
    def get_context_data(self, **kwargs):
        # 継承元（DetailView）のget_context_dataを呼んで、contextを取得。
        context = super().get_context_data(**kwargs)
        plant = context["plant_detail"]
        context["watering_state"] = get_watering_state(
            plant.last_watering_date, plant.watering_frequency
        )
        return context


# 植物追加
class PlantAddView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.AddPlantForm
    template_name = "plant_management/plant_add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "plant_management:detail", kwargs={"pk": self.object.plant_id}
        )


# 植物編集
class PlantEditView(
    mixins.PlantOwnerOnlyMixin, LoginRequiredMixin, generic.UpdateView
):
    model = Plant
    form_class = forms.EditPlantForm
    template_name = "plant_management/plant_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plant = Plant.objects.get(pk=self.kwargs["pk"])
        context["plant_name"] = plant.name
        return context

    def get_success_url(self):
        return reverse_lazy(
            "plant_management:detail", kwargs={"pk": self.object.plant_id}
        )


# 植物削除
class PlantDeleteView(
    mixins.PlantOwnerOnlyMixin, LoginRequiredMixin, generic.DeleteView
):
    template_name = "plant_management/plant_delete.html"
    model = Plant
    success_url = reverse_lazy("plant_management:list")


# 関連URL追加
class RelatedUrlAddView(
    mixins.RelatedPlantOwnerOnlyMixin, LoginRequiredMixin, generic.CreateView
):
    form_class = forms.AddRelatedUrlForm
    template_name = "plant_management/related_url_add.html"

    def form_valid(self, form):
        plant = Plant.objects.get(pk=self.kwargs.get("plant_id"))
        form.instance.user = self.request.user
        form.instance.plant = plant
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plant = Plant.objects.get(pk=self.kwargs.get("plant_id"))
        context["plant_name"] = plant.name
        return context

    def get_success_url(self):
        return reverse_lazy(
            "plant_management:detail", kwargs={"pk": self.object.plant_id}
        )


# 関連URL削除
class RelatedUrlDeleteView(
    OwnerOnlyMixin, LoginRequiredMixin, generic.DeleteView
):
    template_name = "plant_management/related_url_delete.html"
    model = RelatedURL
    context_object_name = "url_info"

    def get_success_url(self):
        return reverse_lazy(
            "plant_management:detail", kwargs={"pk": self.object.plant_id}
        )
