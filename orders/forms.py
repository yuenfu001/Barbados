from django import forms
from .models import *
from django.core.exceptions import ValidationError


class CompanyCreateOrder(forms.ModelForm):
    class Meta:
        model = OrderCompany
        fields = [
            "trip_no",
            "driver_info",
            "client_type",
            "company_name",
            "cac_no",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "weight",
            "con_type",
            "take_off_location",
            "destination",
        ]
    
    def clean_weight(self):
        check_weight = self.cleaned_data.get("weight")
        if check_weight > 45:
            raise ValidationError(f"{check_weight}Tons exceeds the maximum weight of truck which is 45 Tons")
        return check_weight
        
    def clean_cac_no(self):    
        check_cac_no = self.cleaned_data.get("cac_no")
        if not check_cac_no.startswith("RC") or not check_cac_no.startswith("BN") or not check_cac_no[2:].isdigit() or len(check_cac_no) == 6:
            raise ValidationError("CAC number must be in the format 'RC' or 'BN' followed by 6 digits e.g RC345213 or BN675543 ")
        return check_cac_no  


class CompanyUpdateOrder(forms.ModelForm):
    class Meta:
        model = OrderCompany
        fields = [
            "trip_no",
            "driver_info",
            "client_type",
            "company_name",
            "cac_no",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "weight",
            "con_type",
            "take_off_location",
            "destination",
        ]

    def clean_weight(self):
        check_weight = self.cleaned_data.get("weight")
        if check_weight > 45:
            raise ValidationError(f"{check_weight}Tons exceeds the maximum weight of truck which is 45 Tons")
        return check_weight

class IndividualCreateOrder(forms.ModelForm):
    class Meta:
        model = OrderIndividual
        fields = [
            "trip_no",
            "driver_info",
            "client_type",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "weight",
            "con_type",
            "take_off_location",
            "destination",
        ]

    def clean_weight(self):
        check_weight = self.cleaned_data.get("weight")
        if check_weight > 45:
            raise ValidationError(f"{check_weight}Tons exceeds the maximum weight of truck which is 45 Tons")
        return check_weight

class IndividualUpdateOrder(forms.ModelForm):
    class Meta:
        model = OrderIndividual
        fields = [
            "trip_no",
            "driver_info",
            "client_type",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "id_type",
            "id_number",
            "weight",
            "con_type",
            "take_off_location",
            "destination",
        ]

    def clean_weight(self):
        check_weight = self.cleaned_data.get("weight")
        if check_weight > 45:
            raise ValidationError(f"{check_weight}Tons exceeds the maximum weight of truck which is 45 Tons")
        return check_weight
