from django.urls import path
from . import views

app_name = 'plant_management'

urlpatterns = [
    # 植物一覧
    path('list', views.PlantListView.as_view(), name='list'),
    # 水やり完了
    path('watering-complete/<int:pk>', views.complete_watering, name='watering-complete')
]
