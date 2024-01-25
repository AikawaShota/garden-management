from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('lend:equipment-list')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return redirect(self.get_success_url())


class LoginView(LoginView):
    template_name = 'authentication/login.html'
    authentication_form = forms.LoginForm


class LogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    next_page = 'authentication:logout'


# パスワード変更画面
class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = forms.CustomPasswordChangeForm
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('authentication:password-change-done')


# パスワード変更完了画面
class PasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
