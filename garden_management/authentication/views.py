from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView
)


# ユーザ登録
class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy("plant_management:list")

    def form_valid(self, form):
        # 継承元のform_validを呼び出してuserを保存するための返り値を取得。
        response = super().form_valid(form)
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        print(email, type(email))
        print(password, type(password))
        # authenticate関数はusernameとpassword認証が行い、有効だった場合はUserオブジェクトを返す。
        user = authenticate(request=self.request, username=email, passowrd=password)
        print(user)
        # userオブジェクトがNoneかどうかの判定。
        if user is not None:
            # login関数でユーザをログインさせる。
            login(self.request, user)
        else:
            # userオブジェクトがNoneの場合の処理。
            pass
        return response


# ログイン
class LoginView(LoginView):
    template_name = "authentication/login.html"
    authentication_form = forms.LoginForm


# ログアウト
class LogoutView(LogoutView):
    template_name = "authentication/logout.html"
    next_page = "authentication:logout"


# ユーザ情報表示
class UserInformationView(LoginRequiredMixin, TemplateView):
    template_name = "authentication/user_information.html"


# パスワード変更画面
class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = forms.CustomPasswordChangeForm
    template_name = "authentication/password_change.html"
    success_url = reverse_lazy("authentication:password-change-done")


# パスワード変更完了画面
class PasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "authentication/password_change_done.html"
