from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_name', 'is_active', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'user_name',),
            }
        ),
    )

    list_display = ('user_id', 'user_name', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('user_id',)


CustomUser = get_user_model()

admin.site.register(CustomUser, CustomUserAdmin)
