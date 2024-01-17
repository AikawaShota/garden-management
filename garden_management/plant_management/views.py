from django.views import generic
from . import models
# from . import forms


# 植物一覧（水やり状態）
class PlantListView(generic.ListView):
    model = models.Plant
    template_name = 'plant_management/plant-list.html'
    context_object_name = 'plants'
