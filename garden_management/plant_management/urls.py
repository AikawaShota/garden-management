from django.urls import path
from . import views

app_name = 'plant_management'

urlpatterns = [
    # 植物一覧
    path('plant-list', views.PlantListView.as_view(), name='plant-list')
]
