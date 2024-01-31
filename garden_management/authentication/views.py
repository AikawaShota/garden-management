from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
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
        # authenticate関数はusernameとpassword認証が行い、有効だった場合はUserオブジェクトを返す。
        user = authenticate(
            request=self.request, username=email, password=password
        )
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


# ユーザ情報(email, nickname)編集画面
class UserInformationEditView(LoginRequiredMixin, UpdateView):
    template_name = "authentication/user_information_edit.html"
    form_class = forms.UserInformationEditForm
    model = get_user_model()
    success_url = "authentication:user-information"


# パスワード変更画面
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = forms.CustomPasswordChangeForm
    template_name = "authentication/password_change.html"
    success_url = reverse_lazy("authentication:password-change-done")


# パスワード変更完了画面
class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "authentication/password_change_done.html"


# パスワードリセットのメール送信画面
class CustomPasswordResetView(PasswordResetView):
    template_name = "authentication/password_reset.html"
    form_class = forms.CustomPasswordResetForm
    email_template_name = "email/custom_password_reset_email.html"
    subject_template_name = "email/custom_password_reset_subject.txt"
    success_url = reverse_lazy('authentication:password-reset-done')
    from_email = "inquiry@niwakan.mesekit.com"


# パスワードリセットのメール送信後画面
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "authentication/password_reset_done.html"


# パスワードリセットのURLにアクセスした際のパスワード更新画面
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "authentication/password_reset_confirm.html"


# パスワードリセットが完了した際の画面
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "authentication/password_reset_complete.html"
