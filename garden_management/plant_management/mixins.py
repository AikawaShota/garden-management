from . import models
from django.contrib.auth.mixins import UserPassesTestMixin


# ログインユーザとオブジェクトの作成者が同じか判定しアクセス制御を行うクラス。
class OwnerOnlyMixin(UserPassesTestMixin):
    # ログイン中のユーザとオブジェクトを作成したユーザと異なる場合エラーを返す。
    def test_func(self):
        current_user = self.request.user
        current_object = self.get_object()
        return current_user == current_object.user


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
