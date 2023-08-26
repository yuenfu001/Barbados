from django.db import models
from base.models import Name
from trucks.models import TruckInfo
# Create your models here.
class DriverInfo(Name):
    profile_pic = models.ImageField(upload_to="users/")
    assigned_truck = models.ForeignKey(TruckInfo, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Driver Information"
        verbose_name_plural = "Driver Informations"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.fullname.title()}"