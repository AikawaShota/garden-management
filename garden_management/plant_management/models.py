from django.db import models
from django.core.validators import MaxValueValidator


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image_path = models.ImageField(blank=True, null=True)
    watering_frequency = models.DurationField(required=True)
    last_watering_date = models.DateTimeField()
    description = models.CharField(max_length=4095, blank=True, null=True)


class RelatedURL(models.Model):
    related_url_id = models.AutoField(primary_key=True)
    plant_id = models.ForeignKey(
        Plant,
        on_delete = models.CASCADE,
    )
    url = models.URLField(max_length=2047)


class CultivationCalendar(models.Model):
    plant_id = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=4095, blank=True, null=True)
    color_id = models.ForeignKey(
        Color,
        on_delete = models.SET_NULL
    )
    start_at = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(35),)
    )
    end_at = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(35),)
    )


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=63)
    color_code = models.PositiveIntegerField(
        validators=(MaxValueValidator(16777215),)
    )
