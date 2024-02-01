from .functions import send_inquiry_mail, send_inquiry_mail_to_user
from .forms import InquiryForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# 問い合わせフォーム
class InquiryFormView(LoginRequiredMixin, FormView):
    form_class = InquiryForm
    template_name = "help/inquiry_form.html"
    success_url = reverse_lazy("help:inquiry-complete")

    def form_valid(self, form):
        category = form.cleaned_data["category"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        is_send_user = form.cleaned_data["is_send_user"]
        user = self.request.user
        nickname = user.nickname
        user_email = user.email
        send_inquiry_mail(category, subject, message, nickname, user_email)
        if is_send_user:
            send_inquiry_mail_to_user(
                category, subject, message, nickname, user_email
            )
        return super().form_valid(form)


# 問い合わせ完了
class InquiryCompleteView(LoginRequiredMixin, TemplateView):
    template_name = "help/inquiry_complete.html"
