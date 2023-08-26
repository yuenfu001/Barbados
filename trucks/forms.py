from .models import *
from django import forms
from django.db.models import Q

class TruckCreate(forms.ModelForm):
    class Meta:
        model = TruckInfo
        fields = ["bl_number", "plate_number"]


    def clean(self):
        cleaned_data = super().clean()
        truck_no = cleaned_data.get("bl_number")
        plate_number = cleaned_data.get("plate_number")
        truck_id = self.instance.id
        if TruckInfo.objects.exclude(id=truck_id).filter(Q(bl_number__iexact=truck_no)).exists():
            raise forms.ValidationError(f"The {truck_no} is already in use.")
        
        elif TruckInfo.objects.exclude(id=truck_id).filter(Q(plate_number__iexact=plate_number)).exists():
            raise forms.ValidationError(f"The plate number '{plate_number}' already exists.")
        return cleaned_data
    
    
class TruckUpdate(forms.ModelForm):
    class Meta:
        model = TruckInfo
        fields = ["bl_number", "plate_number"]

    def clean(self):
        cleaned_data = super().clean()
        truck_no = cleaned_data.get("bl_number")
        plate_number = cleaned_data.get("plate_number")
        truck_id = self.instance.id
        if TruckInfo.objects.exclude(id=truck_id).filter(bl_number=truck_no).exists():
            raise forms.ValidationError("The truck number is already in use.")
        
        elif TruckInfo.objects.exclude(id=truck_id).filter(plate_number=plate_number).exists():
            raise forms.ValidationError(f"The plate number '{plate_number}' already exists.")
        return cleaned_data
