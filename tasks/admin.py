from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Task

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'mobile', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('mobile',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Task)
