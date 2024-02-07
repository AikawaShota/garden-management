from . import forms
from utilities.mixins import LoginUserOnlyMixin
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
    """ユーザ登録を行うView。

    CreateViewを継承し、ユーザモデルにユーザを新規登録します。

    Note:
        form_valid内で、正しくユーザ登録が行われた場合に自動的にログインする処理を行っています。
        ログイン後はsuccess_urlに格納されているurlに遷移します。

    Attributes:
        form_class(obj): ユーザ登録に利用するFormを格納します。
        template_name(str): ユーザ登録に利用するtemplateまでのパスを格納します。
        success_url(str): ユーザ登録処理が正常に終了した場合の遷移先URLを格納します。
    """

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
class CustomLoginView(LoginView):
    """ログインフォームの表示とログイン処理を行うView。

    LoginViewを継承し、ログイン処理を行っています。

    Attributes:
        template_name(str): ユーザ登録に利用するtemplateまでのパスを格納します。
        authentication_form(obj): ログイン時に利用するFormを指定します。
    """
    template_name = "authentication/login.html"
    authentication_form = forms.LoginForm


# ログアウト
class CustomLogoutView(LogoutView):
    """ログアウト処理を行うView。

    LogoutViewを継承し、ログアウト処理を行っています。

    Attributes:
        template_name(str): ログアウト時に利用するtemplateまでのパスを格納します。
        next_page(str): ログアウト処理が完了した際の遷移先を指定します。
    """
    template_name = "authentication/logout.html"
    next_page = "authentication:logout"


# ユーザ情報表示
class UserInformationView(LoginRequiredMixin, TemplateView):
    """ユーザ情報の表示をするView。

    TemplateViewを継承し、templateを指定しています。

    Note:
        LoginRequiredMixinを継承しているため、ログイン時のみアクセス可能です。
        ユーザ情報の取得・表示はtemplate側で行っています。
    Attributes:
        template_name(str): ユーザ情報表示に利用するtemplateまでのパスを格納します。
    """
    template_name = "authentication/user_information.html"


# ユーザ情報編集
class UserInformationEditView(
    LoginUserOnlyMixin,
    LoginRequiredMixin,
    UpdateView
):
    """ユーザ情報の編集を行うView。

    UpdateViewを継承し、ユーザモデルの該当オブジェクトの情報を更新します。

    Note:
        ログイン中のユーザではないユーザ情報が編集できないよう、LoginUserOnlyMixinを継承しています。

    Attributes:
        template_name(str): ユーザ情報編集に利用するtemplateまでのパスを格納します。
        form_class(obj): ユーザ情報編集に利用するFormを格納します。
        model(obj): 更新するモデル(ユーザモデル)を指定します。
        success_url(str): ユーザ情報の更新が成功した場合の遷移先URLを格納します。
    """
    template_name = "authentication/user_information_edit.html"
    form_class = forms.UserInformationEditForm
    model = get_user_model()
    success_url = reverse_lazy("authentication:user-information")


# パスワード変更
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """パスワード変更を行うView。

    PasswordChangeViewを継承し、パスワード変更処理を行います。

    Attributes:
        form_class(obj): パスワード変更に利用するFormを指定します。
        template_name(str): パスワード変更に利用するtemplateまでのパスを格納します。
        success_url(str): パスワード変更処理が成功した場合の遷移先URLを格納します。
    """
    form_class = forms.CustomPasswordChangeForm
    template_name = "authentication/password_change.html"
    success_url = reverse_lazy("authentication:password-change-done")


# パスワード変更完了
class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """パスワード変更完了画面を表示するView。

    PasswordChangeDoneViewを継承し、パスワード変更処理が成功した場合にこのクラスで指定したtemplateを表示する。

    Attributes:
        template_name(str): 表示するtemplateまでのパスを格納する。
    """
    template_name = "authentication/password_change_done.html"


# パスワードリセット用のメール送信
class CustomPasswordResetView(PasswordResetView):
    """パスワードリセット用メールを送信するView。

    PasswordResetViewを継承し、送信先メールアドレスの入力フォームを表示する。
    メールアドレスが有効な場合、パスワードリセット用URLが記載されたメールを送信する。

    Attributes:
        template_name(str): 利用するtemplateまでのパスを格納する。
        form_class(obj): 送信先メールアドレスの入力Formを格納する。
        from_email(str): メールの送信元アドレスを指定する。
        subject_template_name(str): メールの件名のtemplateまでのパスを格納する。
        email_template_name(str): メール本文のtemplateまでのパスを格納する。
        success_url(str): メール送信が成功した場合の遷移先URLを格納する。
    """
    template_name = "authentication/password_reset.html"
    form_class = forms.CustomPasswordResetForm
    from_email = "inquiry@niwakan.mesekit.com"
    subject_template_name = "email/custom_password_reset_subject.txt"
    email_template_name = "email/custom_password_reset_email.html"
    success_url = reverse_lazy('authentication:password-reset-done')


# パスワードリセット用のメール送信完了
class CustomPasswordResetDoneView(PasswordResetDoneView):
    """パスワードリセットメール送信完了画面を表示するView。

    パスワードリセットメールの送信が成功した場合に表示するtemplateを指定する。

    Attributes:
        template_name(str): 利用するtemplateまでのパスを格納する。
    """
    template_name = "authentication/password_reset_done.html"


# パスワードリセット用URLにアクセスした際のパスワード登録
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """パスワードリセット時にパスワード再登録フォームを表示するView。

    メールに記載されたパスワードリセット用URLにアクセスした際にパスワード登録フォームを表示します。

    Attributes:
        template_name(str): パスワード再登録に利用するtemplateまでのパスを格納する。
        form_class(obj): パスワード再登録に利用するFormを格納する。
        success_url(str): パスワード再登録が成功した際の遷移先URLを格納する。
    """
    template_name = "authentication/password_reset_confirm.html"
    form_class = forms.CustomPasswordSetForm
    success_url = reverse_lazy("authentication:password-reset-complete")


# パスワードリセット完了
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """パスワードリセット完了画面を表示するView。

    PasswordResetCompleteViewを継承していますが、TemplateViewで代用可能です。
    パスワードの再登録が成功した場合に表示するtemplateを指定します。

    Attributes:
        template_name(str): 利用するtemplateまでのパスを格納します。
    """
    template_name = "authentication/password_reset_complete.html"
