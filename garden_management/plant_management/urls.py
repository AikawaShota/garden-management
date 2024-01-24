from django.urls import path
from . import views

app_name = 'plant_management'

urlpatterns = [
    # 植物一覧
    path('list', views.PlantListView.as_view(), name='list'),
    # 水やり完了
    path('watering-complete/<int:pk>', views.complete_watering, name='watering-complete'),
    # 植物詳細
    path('detail/<int:pk>', views.PlantDetailView.as_view(), name='detail'),
    # 植物追加
    path('add', views.PlantAddView.as_view(), name='add'),
    # 植物編集
    path('edit/<int:pk>', views.PlantEditView.as_view(), name='edit'),
    # 植物削除
    path('delete/<int:pk>', views.PlantDeleteView.as_view(), name='delete'),
    # 関連url追加
    path('add-url/<int:plant_id>', views.RelatedUrlAddView.as_view(), name='add-url'),
]
