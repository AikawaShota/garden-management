# Generated by Django 4.2.7 on 2024-01-17 03:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('color_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(16777215)])),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('path', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('plant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('watering_frequency', models.DurationField()),
                ('last_watering_date', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=4095, null=True)),
                ('is_active', models.BooleanField()),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plant_management.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='RelatedURL',
            fields=[
                ('related_url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=2047)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant_management.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'RelatedURL',
                'verbose_name_plural': 'RelatedURLs',
            },
        ),
        migrations.CreateModel(
            name='PlantOrder',
            fields=[
                ('plant_order_id', models.CharField(primary_key=True, serialize=False)),
                ('priority', models.PositiveSmallIntegerField()),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant_management.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PlantOrders',
            },
        ),
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('image_tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant_management.image')),
            ],
            options={
                'verbose_name': 'ImageTag',
                'verbose_name_plural': 'ImageTags',
            },
        ),
        migrations.CreateModel(
            name='CultivationCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=4095, null=True)),
                ('start_at', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(35)])),
                ('end_at', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(35)])),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plant_management.color')),
                ('plant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plant_management.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CultivationCalendar',
                'verbose_name_plural': 'CultivationCalendars',
            },
        ),
    ]
