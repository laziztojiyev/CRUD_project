from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser


# Register your models here.

class ConfiguredFields(BaseUserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_staff', 'phone_number']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'image', 'phone_number')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide   ',),
            'fields': ('username', 'password1', 'password2', 'image', 'phone_number'),
        }),
    )


@admin.register(CustomUser)
class UserAdmin(ConfiguredFields):
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


admin.site.unregister(Group)