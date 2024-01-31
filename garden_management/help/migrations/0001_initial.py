# Generated by Django 4.2.7 on 2024-01-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InquiryCategory',
            fields=[
                ('inquiry_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('priority', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'InquiryCategory',
                'verbose_name_plural': 'InquiryCategories',
            },
        ),
    ]