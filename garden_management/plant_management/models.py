from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    alt = models.CharField(max_length=255)
    path = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.alt


class ImageTag(models.Model):
    image_tag_id = models.AutoField(primary_key=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ImageTag'
        verbose_name_plural = 'ImageTags'

    def __str__(self):
        return self.name


class Plant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    watering_frequency = models.DurationField()
    last_watering_date = models.DateTimeField()
    description = models.TextField(max_length=4095, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name


class RelatedURL(models.Model):
    related_url_id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
    )
    url = models.URLField(max_length=2047)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'RelatedURL'
        verbose_name_plural = 'RelatedURLs'

    def __str__(self):
        return self.url


class PlantOrder(models.Model):
    plant_order_id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )
    priority = models.PositiveSmallIntegerField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'PlantOrder'
        verbose_name_plural = 'PlantOrders'

    def __str__(self):
        return f'user:{self.user}, plant:{self.plant}, {self.priority}'


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color_code = models.PositiveIntegerField(
        validators=(MaxValueValidator(16777215),)
    )

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name


class CultivationCalendar(models.Model):
    cultivation_calendar_id = models.AutoField(primary_key=True)
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4095, blank=True, null=True)
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    start_at = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(35),)
    )
    end_at = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(35),)
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'CultivationCalendar'
        verbose_name_plural = 'CultibationCalendars'

    def __str__(self):
        return self.title
