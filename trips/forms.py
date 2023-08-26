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
        trip_no = cleaned_data.get("Trip_no")
        trip_id = self.instance.id
        if IndividualTrips.objects.exclude(id=trip_id).filter(Trip_no=trip_no).exists():
            raise forms.ValidationError("The trip number is already in use.")
        
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
        
        if CompanyTrips.objects.exclude(id=trip_id).filter(Trip_no=calculated_trip_no).exists():
            raise forms.ValidationError("The trip number is already in use.")
        
        return cleaned_data