from . import models
from django.contrib import admin


@admin.register(models.ImageCategory)
class ImageCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'alt')


@admin.register(models.ImageTag)
class ImageTagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('plant_id', 'name')


@admin.register(models.RelatedURL)
class RelatedURLAdmin(admin.ModelAdmin):
    list_display = ('related_url_id', 'name', 'url')


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CultivationCalendar)
class CultivationCalendarAdmin(admin.ModelAdmin):
    pass
