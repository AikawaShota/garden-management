from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'authentication'

urlpatterns = [
    # /authenticationにアクセスした場合は、ログインページにリダイレクト。
    path('', RedirectView.as_view(url='/authentication/login')),
    # ユーザ登録
    path('signup', views.SignUpView.as_view(), name='signup'),
    # ログイン
    path('login', views.LoginView.as_view(), name='login'),
    # ログアウト
    path('logout', views.LogoutView.as_view(), name='logout'),
    # パスワード変更
    path('password-change', views.PasswordChangeView.as_view(), name='password-change'),
    # パスワード変更完了画面
    path('password-change/done', views.PasswordChangeDoneView.as_view(), name='password-change-done'),
]
