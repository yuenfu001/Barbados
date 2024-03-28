from django import forms
from .models import *
from django.core.exceptions import ValidationError

class DriverCreate(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = [
            "profile_pic",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "assigned_truck",
        ]

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        middle_name = self.cleaned_data.get("middle_name")
        truck = self.cleaned_data.get("assigned_truck")
        cell = self.cleaned_data.get("phone_number")
        id_no = self.cleaned_data.get("id_number")
        driver_id = self.instance.id  # Get the ID of the driver being updated

        # Check if any other driver has the same email
        if (
            DriverInfo.objects.exclude(id=driver_id)
            .filter(first_name=first_name, last_name=last_name, middle_name=middle_name)
            .exists()
        ):
            raise forms.ValidationError(
                "The first name and last name you entered is already in use by another driver."
            )

        elif (
            DriverInfo.objects.exclude(id=driver_id)
            .filter(assigned_truck=truck)
            .exists()
        ):
            raise forms.ValidationError(
                "The assigned Truck you entered is already in use by another driver."
            )

        elif (
            DriverInfo.objects.exclude(id=driver_id).filter(phone_number=cell).exists()
        ):
            raise forms.ValidationError(
                "The phone number you entered belongs to another driver."
            )

        elif DriverInfo.objects.exclude(id=driver_id).filter(id_number=id_no).exists():
            raise forms.ValidationError(
                "The ID Number you entered belongs to another driver."
            )

        return cleaned_data
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Additional logic or modifications before saving
        if commit:
            instance.save()
        return instance


class DriverUpdate(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = [
            "profile_pic",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "assigned_truck",
        ]

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        middle_name = self.cleaned_data.get("middle_name")
        truck = self.cleaned_data.get("assigned_truck")
        cell = self.cleaned_data.get("phone_number")
        id_no = self.cleaned_data.get("id_number")
        driver_id = self.instance.id  # Get the ID of the driver being updated

        # Check if any other driver has the same email
        if (
            DriverInfo.objects.exclude(id=driver_id)
            .filter(first_name=first_name, last_name=last_name, middle_name=middle_name)
            .exists()
        ):
            raise forms.ValidationError(
                "The first name and last name you entered is already in use by another driver."
            )

        elif (
            DriverInfo.objects.exclude(id=driver_id)
            .filter(assigned_truck=truck)
            .exists()
        ):
            raise forms.ValidationError(
                "The assigned Truck you entered is already in use by another driver."
            )

        elif (
            DriverInfo.objects.exclude(id=driver_id).filter(phone_number=cell).exists()
        ):
            raise forms.ValidationError(
                "The phone number you entered belongs to another driver."
            )

        elif DriverInfo.objects.exclude(id=driver_id).filter(id_number=id_no).exists():
            raise forms.ValidationError(
                "The ID Number you entered belongs to another driver."
            )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Additional logic or modifications before saving
        if commit:
            instance.save()
        return instance
