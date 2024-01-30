from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# adminサイトでのCustomUserModelの表示をカスタマイズ。
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None, {
                "fields": (
                    "email",
                    "password",
                    "nickname",
                    "is_active",
                    "date_joined"
                )
            }
        ),
        (
            "Permissions", {
                "fields": ("is_staff", "is_superuser")
            }
        )
    )

    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "nickname",)
            }
        ),
    )

    list_display = ("user_id", "nickname", "email")
    list_filter = ("is_staff", "is_active")
    ordering = ("user_id",)


# カスタムユーザモデルを取得。
CustomUser = get_user_model()

# カスタムユーザモデルをAdminサイトに登録。
admin.site.register(CustomUser, CustomUserAdmin)
