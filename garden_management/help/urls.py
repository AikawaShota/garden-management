from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'help'

urlpatterns = [
    # /helpにアクセスした場合は、お問い合わせページにリダイレクト。
    path('', RedirectView.as_view(url='/help/inquiry')),
    # 問い合わせ
    path('inquiry', views.InquiryFormView.as_view(), name='inquiry'),
    # 問い合わせ完了
    path('inquiry-complete', views.InquiryCompleteView.as_view(), name='inquiry-complete'),
]
