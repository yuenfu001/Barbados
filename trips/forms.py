from django import forms
from .models import *


class IndividualCreateTrips(forms.ModelForm):
    class Meta:
        model = IndividualTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]

class IndividualUpdateTrips(forms.ModelForm):
    class Meta:
        model = IndividualTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        initials = cleaned_data.get("initials")
        date = self.instance.date  # Get the date from the instance
        calculated_trip_no = f"TP/{initials}/{date}"
        trip_id = self.instance.id
        
        # if CompanyTrips.objects.exclude(id=trip_id).filter(name=name).exists():
        #     raise forms.ValidationError("The trip name is already in use.")
        
        if IndividualTrips.objects.exclude(id=trip_id).filter(initials=initials).exists():
            raise forms.ValidationError("The trip initials is already in use.")
        
        # elif CompanyTrips.objects.exclude(id=trip_id).filter(date=date).exists():
        #     raise forms.ValidationError("The trip date is already in use.")
        
        return cleaned_data

class CompanyCreateTrips(forms.ModelForm):
    class Meta:
        model = CompanyTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]

class CompanyUpdateTrips(forms.ModelForm):
    class Meta:
        model = CompanyTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        initials = cleaned_data.get("initials")
        date = self.instance.date  # Get the date from the instance
        calculated_trip_no = f"TP/{initials}/{date}"
        trip_id = self.instance.id
        
        # if CompanyTrips.objects.exclude(id=trip_id).filter(name=name).exists():
        #     raise forms.ValidationError("The trip name is already in use.")
        
        if CompanyTrips.objects.exclude(id=trip_id).filter(initials=initials).exists():
            raise forms.ValidationError("The trip initials is already in use.")
        
        # elif CompanyTrips.objects.exclude(id=trip_id).filter(date=date).exists():
        #     raise forms.ValidationError("The trip date is already in use.")
        
        return cleaned_data