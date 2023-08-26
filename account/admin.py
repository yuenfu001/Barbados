from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = [
        "username", "email", "first_name", "last_name", "is_staff", "is_superuser"
    ]
   

# admin.site.register(UserAdmin)