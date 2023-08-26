
urls.py:

from django.urls import path
from report import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='index'),
    path('add-truck/', views.AddTruck, name='truck'),
    path('update-truck/<str:pk>/', views.UpdateTruck, name='updatetruck'),
    path('add-driver/', views.AddDriver, name='driver'),
    path('update-driver/<str:pk>/', views.UpdateDriver, name='updatedriver'),
    path('delete-driver/<str:delete>/', views.DeleteDriver, name='deletedriver'),
    path('showdrivers/', views.ViewDriver, name='displaydriver'),
    path('driverdetails/<str:pk>/', views.DriverDetails, name='driverdetails'),
    path('addcompanyorder/', views.AddCompanyOrder, name='companyorder'),
    path('update-companyorder/<str:pk>/', views.UpdateCompanyOrder, name='updatecompanyorder'),
    path('viewcompanyorder/', views.ViewCompanyOrder, name='viewcompanyorder'),
    path('companyorderdetails/<str:pk>/', views.CompanyOrderDetails, name='companyorderdetail'),
    path('addindividualorder/', views.AddIndivdualOrder, name='individualorder'),
    path('update-individualorder/<str:pk>/', views.UpdateIndividualOrder, name='updateindividualorder'),
    path('viewindividualorder/', views.ViewIndividualOrder, name='viewindividualorder'),
    path('individualorderdetails/<str:pk>/', views.IndividualOrderDetails, name='individualorderdetail'),
    path('add-Itrip/', views.IndividualTripForm, name='individualtrip'),
    path('add-Ctrip/', views.CompanyTripForm, name='companytrip'),
    path('view-Itrip/', views.IndividualTripView, name='viewindividualtrip'),
    path('view-Ctrip/', views.CompanyTripView, name='viewcompanytrip'),
    path('register/', views.Registration, name='register'),
    path('update-user/<str:pk>/', views.UpdateUser, name='updateuser'),
    path('registry/', views.UserRegistry, name='registry'),
    path('user-details/<str:pk>/', views.UserDetails, name='userdetails'),
    path('login/', views.Login, name='login'),
]

views.py:
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError

from .models import *
from .forms import *

def home(request):
    title = "Home Page"
    companyorder = OrderCompany.objects.all().count()
    individualorder = OrderIndividual.objects.all().count()
    companytrips = CompanyTrips.objects.all().count()
    individualtrips = IndividualTrips.objects.all().count()
    truckinfo = TruckInfo.objects.all().count()
    driverinfo = DriverInfo.objects.all().count()
    context = {
        "title": title,
        "truckinfo": truckinfo,
        "driverinfo": driverinfo,
        "iorder": individualorder,
        "corder": companyorder,
        "ctrips": companytrips,
        "itrips": individualtrips,

               
               
               }
    return render(request, "base/index.html", context)

# Create your views here.
def Registration(request):
    register = RegisterForm(request.POST or None)
    if request.method == "POST":
        if register.is_valid():
            register.save()
            messages.success(request,"User successfully added")
            return redirect("/registry")
    context = {
            "register":register
    }
    return render(request, "authentications/register.html", context)

def UserRegistry(request):
    viewuser = User.objects.all()
    context = {
            "registry":viewuser
    }
    return render(request, "display/viewregistry.html", context)

# used the get_user_model from the django.contrib.auth import get_user_model in the forms.py
def UpdateUser(request, pk):
    User = get_user_model()
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateUserForm(request.POST or None, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request,"User successfully updated")
            return redirect("userdetails", pk=pk)
    
    else:
        form = UpdateUserForm(instance=user)
        
    context = {
            "updateuser":form, "user":user
    }
    return render(request, "authentications/updateuser.html", context)

def UserRegistry(request):
    viewuser = User.objects.all()
    context = {
            "registry":viewuser
    }
    return render(request, "display/viewregistry.html", context)

def UserDetails(request, pk):
    details = User.objects.get(id=pk)
    context = {
            "details":details
    }
    return render(request, "display/userdetails.html", context)

def Login(request):
    context = {}
    return render(request, "authentications/login.html", context)




def AddTruck(request):
    title = "Add Truck"
    form = TruckCreate(request.POST or None)
    queryset = TruckInfo.objects.all()
    if request.method == "POST":
        if form.is_valid():
            bl_number = form.cleaned_data["bl_number"]
            if queryset.filter(bl_number=bl_number).exists():
                messages.error(request, "This Truck Number already exist")
                return redirect("/add-truck")
            form.save()
        return redirect("/add-truck")
    context = {"truckform": form, "alltruck": queryset, "title": title}
    return render(request, "forms/truckform.html", context)

def UpdateTruck(request,pk):
    title = "Update Truck"
    queryset = TruckInfo.objects.get(id=pk)
    update = TruckUpdate(request.POST or None, instance=queryset)
    if request.method == "POST":
        if update.is_valid():
            update.save()
        return redirect("/add-truck")
    context = {"updatetruck": update, "alltruck": queryset, "title": title}
    return render(request, "update/trucks.html", context)


def AddDriver(request):
    title = "Add Driver"
    form = DriverCreate(request.POST or None, request.FILES or None)
    query = DriverInfo.objects.all()
    if request.method == "POST":
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            if query.filter(first_name=first_name, last_name=last_name):
                messages.error(request, "This Driver already exists")
                return redirect("/add-driver")
            else:
                form.save()
                messages.success(request, "This Driver add successfully")
                return redirect("/showdrivers")
    context = {"driverform": form, "title": title}
    return render(request, "forms/driver_form.html", context)

def ViewDriver(request):
    title = "View Driver"
    queryset = DriverInfo.objects.all()

    context = {"alldriver": queryset, "title": title}
    return render(request, "display/driver.html", context)

def DriverDetails(request, pk):
    title = "Driver Details"
    unique = DriverInfo.objects.get(id=pk)

    context = {"details": unique, "title": title}
    return render(request, "display/driverdetails.html", context)


def UpdateDriver(request,pk):
    title = "Update Driver"
    queryset = DriverInfo.objects.all()
    query = DriverInfo.objects.get(id=pk)
    update = DriverUpdate(request.POST or None, request.FILES or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            
                update.save()
                messages.success(request, "Update successfully")
                return redirect("driverdetails", pk=pk)
    context = {"updatedriver": update, "title": title}
    return render(request, "update/driverdetails.html", context)


# handle foreignkey that is protected
def DeleteDriver(request, delete):
    title = "Delete Driver"
    try:
        tag = "Are you sure you want to delete this entry ?"
        query = DriverInfo.objects.get(id=delete)
        if request.method == "POST":
            query.delete()
            messages.success(request,"Successfully Deleted")
            return redirect("displaydriver")
        context ={
                "tags":tag, "title":title
        }
        return render(request, "display/delete.html", context)
        
    except ProtectedError as e:
        protected_references = []
        for i in e.protected_objects:
            if isinstance(i, OrderCompany):
                protected_references.append(f"{i.trip_no}")
        error_message = f"This driver can't be deleted as he is used in a particular Order: " + ", ".join(protected_references)
        context ={
             "msg":error_message
        }
        return render(request,"display/error.html", context)
def AddCompanyOrder(request):
    title = "Add Order"
    form = CompanyCreateOrder(request.POST or None)
    queryset = OrderCompany.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New Order added")
        return redirect("viewcompanyorder")
    context = {"companyorder": form, "allorders": queryset, "title": title}
    return render(request, "forms/companyorderform.html", context)


def ViewCompanyOrder(request):
    title = "Order"
    # form = CompanyCreateOrder(request.POST or None)
    queryset = OrderCompany.objects.all()
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "New Order added")
    #     return redirect("/driver")
    context = {"vieworders": queryset, "title": title}
    return render(request, "display/Companyorder.html", context)


def CompanyOrderDetails(request, pk):
    title = "Order Details"
    queryset = OrderCompany.objects.get(id=pk)
    
    context = {"orderdetails": queryset, "title": title}
    return render(request, "reports/companyorderdetail.html", context)

def UpdateCompanyOrder(request, pk):
    title = "Update Order"
    query = OrderCompany.objects.get(id=pk)
    update = CompanyUpdateOrder(request.POST or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            return redirect("companyorderdetail", pk=pk)
    context = {"updateorder": update, "title": title}
    return render(request, "update/individualdetails.html", context)

def CompanyTripForm(request):
    title = "Trips"
    queryset = CompanyTrips.objects.all()
    form = CompanyCreateTrips(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            initials = form.cleaned_data["initials"]
            if queryset.filter(initials=initials).exists():
                messages.error(request, "This Trip Name already exists")
                return redirect("/add-Ctrip")
            else:
                form.save()
                messages.success(request, "New Trip added successfully")
                return redirect("/view-Ctrip")
    context = {"trip": form, "title": title, "added": queryset}
    return render(request, "forms/ctrips.html", context)


def CompanyTripView(request):
    title = "Trips"
    queryset = CompanyTrips.objects.all()
   
    context = {"title": title, "added": queryset}
    return render(request, "display/ctrip.html", context)


# A form to display individual order
def AddIndivdualOrder(request):
    title = "Add Order"
    form = IndividualCreateOrder(request.POST or None)
    queryset = OrderIndividual.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New Order added")
        return redirect("viewindividualorder")
    context = {"individualorder": form, "allorders": queryset, "title": title}
    return render(request, "forms/individualorderform.html", context)

def ViewIndividualOrder(request):
    title = "Individual Order"
    # form = CompanyCreateOrder(request.POST or None)
    queryset = OrderIndividual.objects.all()
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "New Order added")
    #     return redirect("/driver")
    context = {"vieworders": queryset, "title": title}
    return render(request, "display/Individualorder.html", context)

def IndividualOrderDetails(request, pk):
    title = "Order Details"
    queryset = OrderIndividual.objects.get(id=pk)

    context = {"orderdetails": queryset, "title": title}
    return render(request, "reports/individualorderdetail.html", context)

def UpdateIndividualOrder(request,pk):
    title = "Update Order"
    queryset = OrderIndividual.objects.get(id=pk)
    update = IndividualUpdateOrder(request.POST or None, instance=queryset)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            messages.success(request, "Order Updated")
            return redirect("individualorderdetail", pk=pk)
    context = {"updateorder": update, "title": title}
    return render(request, "update/individualdetails.html", context)

def IndividualTripForm(request):
    title = "Trips"
    query = IndividualTrips.objects.all()
    iform = IndividualCreateTrips(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if iform.is_valid():
            initials = iform.cleaned_data["initials"]
            if query.filter(initials=initials).exists():
                messages.error(request, "This Trip Name already exists")
                return redirect("/add-Ctrip")
            else:
                iform.save()
                messages.success(request, "New Trip added successfully")
                return redirect("/view-Itrip")
    context = {"itrip": iform, "title": title, "iadded": query}
    return render(request, "forms/itrip.html", context)

def IndividualTripView(request):
    title = "Trips"
    query = IndividualTrips.objects.all()
    
   
    context = {"title": title, "iadded": query}
    return render(request, "display/itrip.html", context)


def PrintIndividualOrderDetails(request, pk):
    title = "Order Details"
    queryset = OrderIndividual.objects.get(id=pk)

    context = {"orderdetails": queryset, "title": title}
    return render(request, "reports/individualorderdetail.html", context)

models.py:
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class TruckInfo(models.Model):
    bl_number = models.CharField(max_length=20)
    plate_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Truck Informantion"
        verbose_name_plural = "Truck Information"

    def __str__(self):
        return f"{self.bl_number}"


class Name(models.Model):
    ID = (("DL", "Driver's License"), ("IP", "Int'l Passport"), ("NI", "NIN"))
    first_name = models.CharField(max_length=50, help_text="Enter Name of client")
    last_name = models.CharField(max_length=50, help_text="Enter SurName of client")
    middle_name = models.CharField(
        max_length=50, help_text="Enter Middle Name of client", blank=True, null=True
    )
    id_type = models.CharField(max_length=3, choices=ID)
    id_number = models.CharField(max_length=11)
    phone_number = models.CharField(
        max_length=11, help_text="Enter representative's Phone Number, 11 digits"
    )

    @property
    def fullname(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"


class DriverInfo(Name):
    profile_pic = models.ImageField(upload_to="users/")
    assigned_truck = models.ForeignKey(TruckInfo, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Driver Information"
        verbose_name_plural = "Driver Informations"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.fullname.title()}"

class IndividualTrips(models.Model):
    CHOICES = (("TP","TRIP"),)
    name =  models.CharField(max_length=2, choices=CHOICES, default="TP")
    initials =  models.CharField(max_length=5, help_text="Enter Fullname Initials")
    date = models.DateField(auto_now_add=True)
    proposal = models.FileField(upload_to="proposals/")

    @property
    def Trip_no(self):
        return f"{self.name}/{self.initials}/{self.date}"
    
    def __str__(self):
        return f"{self.Trip_no}"

class CompanyTrips(models.Model):
    CHOICES = (("TP","TRIP"),)
    name =  models.CharField(max_length=2, choices=CHOICES, default="TP")
    initials =  models.CharField(max_length=5, help_text="Enter Company Name Initials")
    date = models.DateField(auto_now_add=True)
    proposal = models.FileField(upload_to="proposals/")

    @property
    def Trip_no(self):
        return f"{self.name}/{self.initials}/{self.date}"
    
    def __str__(self):
        return f"{self.Trip_no}"
    

class OrderCompany(Name):
    CLIENT_TYPE = (("C", "Company"),)
    client_type = models.CharField(max_length=15, choices=CLIENT_TYPE, default="I")
    company_name = models.CharField(max_length=100, blank=False, null=True)
    cac_no = models.CharField(max_length=10, blank=True, null=True)
    trip_no = models.ForeignKey('CompanyTrips', on_delete=models.PROTECT)
    driver_info = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(45.00)])
    con_type = models.CharField(max_length=100)
    take_off_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "CompanyOrder"
        verbose_name_plural = "CompanyOrders"
        ordering = ["company_name"]


    def __str__(self):
        return f"{self.driver_info.fullname.title()} {self.driver_info.assigned_truck.bl_number.upper()} {self.driver_info.assigned_truck.plate_number.upper()} {self.weight} {self.con_type.title()}  {self.take_off_location.title()}"


class OrderIndividual(Name):
    CLIENT_TYPE = (("I", "Individual"),)
    client_type = models.CharField(max_length=15, choices=CLIENT_TYPE, default="I")
    trip_no = models.ForeignKey('IndividualTrips', on_delete=models.PROTECT)
    driver_info = models.ForeignKey(DriverInfo, on_delete=models.SET_NULL, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4)
    con_type = models.CharField(max_length=100)
    take_off_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "IndividualOrder"
        verbose_name_plural = "IndividualOrders"

    
    def __str__(self):
        return f"{self.driver_info.fullname} {self.driver_info.assigned_truck.bl_number} {self.driver_info.assigned_truck.plate_number} {self.weight} {self.con_type}  {self.take_off_location} {self.date_joined} {self.date_modified}"

forms.py:
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

# from django.models import models
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    is_staff = forms.BooleanField(label="Give user staff permissions", required=False)
    is_superuser = forms.BooleanField(
        label="Give user admin permission", required=False
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "is_staff",
            "is_superuser",
            "is_active"
        ]


# added UserChangeForm by importing from django.contrib.auth.forms
# aslo used the get_user_model() instead of the User by importing from django.contrib.auth import get_user_model()
class UpdateUserForm(UserChangeForm):
    is_staff = forms.BooleanField(label="Give user staff permissions", required=False)
    is_superuser = forms.BooleanField(
        label="Give user admin permission", required=False
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "is_active"
        ]
        # exclude = ["password1", "password2"]


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
        cleaned_date = super().clean()
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

        return cleaned_date

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Additional logic or modifications before saving
        if commit:
            instance.save()
        return instance


class TruckCreate(forms.ModelForm):
    class Meta:
        model = TruckInfo
        fields = ["bl_number", "plate_number"]


class TruckUpdate(forms.ModelForm):
    class Meta:
        model = TruckInfo
        fields = ["bl_number", "plate_number"]

    def clean(self):
        cleaned_date = super().clean()
        truck_no = self.cleaned_data.get("bl_number")
        plates = self.cleaned_data.get("plate_number")
        truck_id = self.instance.id  # Get the ID of the driver being updated

        # Check if any other driver has the same email
        if TruckInfo.objects.exclude(id=truck_id).filter(bl_number=truck_no).exists():
            raise forms.ValidationError(
                "The truck number you entered is already in use by another driver."
            )

        elif (
            TruckInfo.objects.exclude(id=truck_id).filter(plate_number=plates).exists()
        ):
            raise forms.ValidationError(
                "The Plate number you entered is already in use by another driver."
            )

        return cleaned_date


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


class IndividualCreateTrips(forms.ModelForm):
    class Meta:
        model = IndividualTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]


class CompanyCreateTrips(forms.ModelForm):
    class Meta:
        model = CompanyTrips

        fields = [
            "name",
            "initials",
            "proposal",
        ]
