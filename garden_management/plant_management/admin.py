from . import models
from django.contrib import admin


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImageTag)
class ImageTagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Plant)
class PlantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RelatedURL)
class RelatedURLAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CultivationCalendar)
class CultivationCalendarAdmin(admin.ModelAdmin):
    pass
