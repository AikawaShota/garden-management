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
