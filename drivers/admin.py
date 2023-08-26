from django.contrib import admin
from .models import *
# Register your models here.

class DriverInfoAdmin(admin.ModelAdmin):
    list_display = [
        "fullname",
        "id_type",
        "phone_number",
        "id_number",
        "assigned_truck",
        "date_joined",
        "date_modified",
    ]
   
    list_filter = ["assigned_truck", "date_joined", "date_modified"]

admin.site.register(DriverInfo, DriverInfoAdmin)