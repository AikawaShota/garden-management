<<<<<<< HEAD
# Generated by Django 4.2.7 on 2024-01-27 11:39
=======
# Generated by Django 4.2.7 on 2024-01-28 16:16
>>>>>>> 4ec3bab73065109d6f0fddd28af68870e5848aa4

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plant_management', '0007_alter_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='last_watering_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='plant',
            name='watering_frequency',
            field=models.DurationField(default=datetime.timedelta(days=1)),
        ),
    ]