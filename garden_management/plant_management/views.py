from django.views import generic
from . import models
# from . import forms
import datetime


def get_watering_state(last_watering_date, watering_frequency):
    time_difference = last_watering_date + watering_frequency - datetime.datetime.now()
    return time_difference


# 植物一覧（水やり状態）
class PlantListView(generic.ListView):
    model = models.Plant
    template_name = 'plant_management/plant-list.html'
    context_object_name = 'plants'
