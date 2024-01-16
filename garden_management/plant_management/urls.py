from django.urls import path
from . import views

app_name = 'plant_management'

urlpatterns = [
    path('lists', views.),
]
