from .models import *
from django import forms
from django.db.models import Q
import re

class TruckCreate(forms.ModelForm):
    class Meta:
        model = TruckInfo
        fields = ["bl_number", "plate_number"]

    
    def check_truck(self):
        truck_number = self.cleaned_data.get("bl_number")
        bl_pattern = r"\d{1,3}/\d{1,4}"
        if not re.match(bl_pattern, truck_number):
            raise forms.ValidationError("Invalid Truck number format e.g 21/23 or 234/677 or 1/6789")

        return truck_number
    
    def check_plate(self):
        plate_number = self.cleaned_data.get("plate_number")
        plate_pattern = r"^[A-Za-z]{1,3}-?\d{1,6}[A-za-z]{1,3}$"
        if not re.match(plate_pattern, plate_number):
            raise forms.ValidationError("Invalid plate number format e.g T-12345LA or ABJ-345AK or AKD-04AT")

        return plate_number

    def clean(self):
        cleaned_data = super().clean()
        truck_no = cleaned_data.get("bl_number")
        plate_number = cleaned_data.get("plate_number")
        truck_id = self.instance.id
        
        if TruckInfo.objects.exclude(id=truck_id).filter(Q(bl_number__iexact=truck_no)).exists():
            raise forms.ValidationError(f"The {truck_no} is already in use.")
        
        elif TruckInfo.objects.exclude(id=truck_id).filter(Q(plate_number__iexact=plate_number)).exists():
            raise forms.ValidationError(f"The plate number '{plate_number}' already exists.")
       
        self.check_truck()
        self.check_plate()

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
