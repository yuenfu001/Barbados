from django.db import models

# Create your models here.
class TruckInfo(models.Model):
    bl_number = models.CharField(max_length=7)
    plate_number = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Truck Informantion"
        verbose_name_plural = "Truck Information"

    def __str__(self):
        return f"{self.bl_number} {self.plate_number}"