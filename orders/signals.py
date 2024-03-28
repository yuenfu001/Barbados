from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import OrderCompany, OrderIndividual

@receiver(pre_save, sender=OrderCompany)
def capitalize_Centry(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
    if instance.middle_name is not None:    
        instance.middle_name = instance.middle_name.capitalize()
    instance.company_name = instance.company_name.capitalize()
    instance.con_type = instance.con_type.capitalize()
    instance.take_off_location = instance.take_off_location.capitalize()
    instance.destination = instance.destination.capitalize()


@receiver(pre_save, sender=OrderIndividual)
def capitalize_Ientry(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
    if instance.middle_name is not None: 
        instance.middle_name = instance.middle_name.capitalize()
    instance.con_type = instance.con_type.capitalize()
    instance.take_off_location = instance.take_off_location.capitalize()
    instance.destination = instance.destination.capitalize()