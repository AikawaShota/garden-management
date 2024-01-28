from . import models
from django.contrib import admin


@admin.register(models.InquiryCategory)
class InquiryCategoryAdmin(admin.ModelAdmin):
    pass
