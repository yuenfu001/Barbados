from django.db import models

# Create your models here.
class Name(models.Model):
    ID = (("DL", "Driver's License"), ("IP", "Int'l Passport"), ("NI", "NIN"))
    first_name = models.CharField(max_length=30, help_text="Enter First Name", blank=False, null=False)
    last_name = models.CharField(max_length=30, help_text="Enter SurName e.g Father's Name", blank=False, null=False)
    middle_name = models.CharField(
        max_length=30,default="" ,help_text="Enter Middle Name", blank=True, null=True
    )
    id_type = models.CharField(max_length=3, choices=ID)
    id_number = models.CharField(max_length=12)
    phone_number = models.CharField(
        max_length=11, help_text="Enter representative's Phone Number, 11 digits"
    )
    class Meta:
        abstract = True

    @property
    def fullname(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

