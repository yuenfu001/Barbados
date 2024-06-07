from django.contrib import admin
from .models import *

# Register your models here.


class IndividualTripsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "initials",
        "proposal",
    ]

class CompanyTripsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "initials",
        "proposal",
    ]


admin.site.register(CompanyTrips, CompanyTripsAdmin)
admin.site.register(IndividualTrips, IndividualTripsAdmin)
