from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    # ユーザ登録
    path('signup', views.SignUpView.as_view(), name='signup'),
    # ログイン
    path('login', views.LoginView.as_view(), name='login'),
    # ログアウト
    path('logout', views.LogoutView.as_view(), name='logout'),
]
