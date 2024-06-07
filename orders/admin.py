from django.contrib import admin
from .models import *
# Register your models here.
class OrderCompanyAdmin(admin.ModelAdmin):
    list_display = [
        "trip_no",
        "company_name",
        "cac_no",
        "driver_info",
        "con_type",
        "weight",
        "take_off_location",
        "destination",
        "date_joined",
        "date_modified",
    ]
   
    list_filter = ["company_name", "date_joined", "date_modified"]


class OrderIndividualAdmin(admin.ModelAdmin):
    list_display = [
        "trip_no",
        "fullname",
        "client_type",
        "driver_info",
        "con_type",
        "weight",
        "take_off_location",
        "destination",
        "date_joined",
        "date_modified",
    ]


admin.site.register(OrderCompany, OrderCompanyAdmin)
admin.site.register(OrderIndividual, OrderIndividualAdmin)