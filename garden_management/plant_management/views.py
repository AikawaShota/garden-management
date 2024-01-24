import datetime
from . import models
from . import forms
from . import mixins
from .functions import get_watering_state
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


# 植物一覧（水やり状態）
class PlantListView(LoginRequiredMixin, generic.ListView):
    model = models.Plant
    template_name = 'plant_management/plant_list.html'
    context_object_name = 'plants'

    # 取得するデータをカスタマイズする。
    def get_queryset(self):
        # .filter()：ユーザが作成したオブジェクトのみ取り出す。
        # .order_by()：priorityの値で降順ソートした後、plant_idで昇順ソートする。
        queryset = self.model.objects \
            .select_related('image') \
            .values('plant_id', 'name', 'description', 'image__path', 'image__alt', 'last_watering_date', 'watering_frequency') \
            .filter(user=self.request.user) \
            .order_by('-priority', 'plant_id')
        return queryset

    # 水やりの状態（水やりの要否・次回の水やりまでの時間）を保存するcontextを追加する。
    def get_context_data(self, **kwargs):
        # 継承元（ListView）のget_context_dataを呼んで、contextを取得。
        context = super().get_context_data(**kwargs)
        plants = context['plants']
        for plant in plants:
            plant['watering_state'] = get_watering_state(plant['last_watering_date'], plant['watering_frequency'])
        context['plants'] = plants
        return context


# 水やり完了処理
def complete_watering(request, pk):
    plant = models.Plant.objects.get(pk=pk)
    if plant.user != request.user:
        try:
            raise PermissionDenied()
        except PermissionDenied:
            print('You do not have permission to edit.')
            return redirect('authentication:login')
    plant.last_watering_date = datetime.datetime.now()
    plant.save()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = {
            'watering-state': get_watering_state(plant.last_watering_date, plant.watering_frequency)
        }
    return JsonResponse(data)


# 植物詳細
class PlantDetailView(mixins.OwnerOnlyMixin, LoginRequiredMixin, generic.DetailView):
    model = models.Plant
    template_name = 'plant_management/plant_detail.html'
    context_object_name = 'plant_detail'

    # 水やりの状態（水やりの要否・次回の水やりまでの時間）を保存するcontextを追加する。
    def get_context_data(self, **kwargs):
        # 継承元（DetailView）のget_context_dataを呼んで、contextを取得。
        context = super().get_context_data(**kwargs)
        plant = context['plant_detail']
        context['watering_state'] = get_watering_state(plant.last_watering_date, plant.watering_frequency)
        return context


# 植物追加
class PlantAddView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.PlantForm
    template_name = 'plant_management/plant_add.html'
    success_url = reverse_lazy('plant_management:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
