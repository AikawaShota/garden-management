from django.db import models


# 問い合わせのカテゴリを保存するモデル
class InquiryCategory(models.Model):
    inquiry_category_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    priority = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "InquiryCategory"
        verbose_name_plural = "InquiryCategories"

    def __str__(self):
        return self.name
