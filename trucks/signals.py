from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import TruckInfo


@receiver(pre_save, sender=TruckInfo)
def capitalize_entry(sender, instance, **kwargs):
    instance.plate_number = instance.plate_number.upper()