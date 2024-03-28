from django.db import models

# Create your models here.
class IndividualTrips(models.Model):
    CHOICES = (("TP","TRIP"),)
    name =  models.CharField(max_length=2, choices=CHOICES, default="TP")
    initials =  models.CharField(max_length=5, help_text="Enter Fullname Initials")
    date = models.DateField(auto_now_add=True)
    proposal = models.FileField(upload_to="proposals/")

    class Meta:
        verbose_name = "Individual Trip"
        verbose_name_plural = "Individual Trips"

    @property
    def Trip_no(self):
        return f"{self.name}/{self.id}/{self.initials}/{self.date}"
    
    def __str__(self):
        return f"{self.Trip_no}"

class CompanyTrips(models.Model):
    CHOICES = (("TP","TRIP"),)
    name =  models.CharField(max_length=2, choices=CHOICES, default="TP")
    initials =  models.CharField(max_length=5, help_text="Enter Company Name Initials")
    date = models.DateField(auto_now_add=True)
    proposal = models.FileField(upload_to="proposals/")

    class Meta:
        verbose_name = "Individual Trip"
        verbose_name_plural = "Individual Trips"

    @property
    def Trip_no(self):
        return f"{self.name}/{self.id}/{self.initials}/{self.date}"
    
    def __str__(self):
        return f"{self.Trip_no}"
