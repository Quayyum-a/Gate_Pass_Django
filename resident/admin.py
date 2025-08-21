from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from resident.models import User, House


# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'phone', 'is_resident', 'is_security']
    list_editable = [ 'is_resident', 'is_security']
    list_display_links = ['first_name', 'last_name']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'usable_password','password1', 'password2', 'first_name', 'last_name', 'email', 'phone'),
        }),
    )

    @admin.register(House)
    class HouseAdmin(admin.ModelAdmin):
        list_display = ('house_number', 'address', 'user')