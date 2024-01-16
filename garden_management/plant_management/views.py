from django.views import generic
from . import forms
from . import models


class PlantListView(generic.ListView):
    template_name = 'plant_management/'
