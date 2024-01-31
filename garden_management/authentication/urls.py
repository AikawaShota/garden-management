from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = "authentication"

urlpatterns = [
    # /authenticationにアクセスした場合は、ログインページにリダイレクト。
    path("", RedirectView.as_view(url="/authentication/login")),
    # ユーザ登録
    path("signup", views.SignUpView.as_view(), name="signup"),
    # ログイン
    path("login", views.LoginView.as_view(), name="login"),
    # ログアウト
    path("logout", views.LogoutView.as_view(), name="logout"),
    # ユーザ情報
    path(
        "user-information",
        views.UserInformationView.as_view(),
        name="user-information"
    ),
    # パスワード変更
    path(
        "password-change",
        views.CustomPasswordChangeView.as_view(),
        name="password-change"
    ),
    # パスワード変更完了画面
    path(
        "password-change/done",
        views.CustomPasswordChangeDoneView.as_view(),
        name="password-change-done"
    ),
    # パスワードリセット用メール送信画面
    path(
        "password-reset",
        views.CustomPasswordResetView.as_view(),
        name="password-reset"
    ),
    # パスワードリセット用メール送信後画面
    path(
        "password-reset/done",
        views.CustomPasswordResetDoneView.as_view(),
        name="password-reset-done"
    ),
    # パスワードリセットフォーム画面
    path(
        "password-reset/comfirm/<uidb64>/<token>",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password-reset-confirm"
    ),
    # パスワードリセット完了画面
    path(
        "password-reset/complete",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password-reset-complete"
    )
]
