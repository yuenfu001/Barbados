from django.db import models
from base.models import Name
from drivers.models import DriverInfo
from trips.models import *
from django.core.validators import MaxValueValidator
# Create your models here.
class OrderCompany(Name):
    CLIENT_TYPE = (("C", "Company"),)
    client_type = models.CharField(max_length=15, choices=CLIENT_TYPE, default="I")
    company_name = models.CharField(max_length=100, blank=False, null=True)
    cac_no = models.CharField(max_length=8, blank=True, null=True)
    trip_no = models.ForeignKey(CompanyTrips, on_delete=models.PROTECT)
    driver_info = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    con_type = models.CharField(max_length=100)
    take_off_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Company Order"
        verbose_name_plural = "Company Orders"
        ordering = ["company_name"]


    def __str__(self):
        return f"{self.driver_info.fullname.title()} {self.driver_info.assigned_truck.bl_number.upper()} {self.driver_info.assigned_truck.plate_number.upper()} {self.weight} {self.con_type.title()}  {self.take_off_location.title()}"


class OrderIndividual(Name):
    CLIENT_TYPE = (("I", "Individual"),)
    client_type = models.CharField(max_length=15, choices=CLIENT_TYPE, default="I")
    trip_no = models.ForeignKey(IndividualTrips, on_delete=models.PROTECT)
    driver_info = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    con_type = models.CharField(max_length=100)
    take_off_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Individual Order"
        verbose_name_plural = "Individual Orders"

    
    def __str__(self):
        return f"{self.driver_info.fullname} {self.driver_info.assigned_truck.bl_number} {self.driver_info.assigned_truck.plate_number} {self.weight} {self.con_type}  {self.take_off_location} {self.date_joined} {self.date_modified}"
