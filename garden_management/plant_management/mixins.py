from . import models
from django.contrib.auth.mixins import UserPassesTestMixin


# ログインユーザとPlantオブジェクトの作成者が同じか判定しアクセス制御を行うクラス。
class PlantOwnerOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        plant = models.Plant.objects.get(pk=self.kwargs["pk"])
        return plant.user == self.request.user


# ログインユーザと関連するPlantオブジェクトの作成者が同じか判定しアクセス制御を行うクラス。
class RelatedPlantOwnerOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        plant = models.Plant.objects.get(pk=self.kwargs.get("plant_id"))
        return plant.user == self.request.user
