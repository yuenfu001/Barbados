from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError
from django.contrib.auth import views as auth_views
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator
from django.shortcuts import render
# admins.py
from django.contrib import admin
from django.contrib.auth.models import User
# used to customize the user interface in the admin panel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.models import models

from orders.models import OrderCompany, OrderIndividual
from base.models import Name
from drivers.models import DriverInfo
from trips.models import CompanyTrips, IndividualTrips
from trucks.models import TruckInfo

from account.forms import UpdateUserForm, RegisterForm
from orders.forms import CompanyCreateOrder,CompanyUpdateOrder,IndividualCreateOrder,IndividualUpdateOrder
from trucks.forms import TruckCreate, TruckUpdate
from trips.forms import CompanyCreateTrips, IndividualCreateTrips
from drivers.forms import DriverCreate,DriverUpdate


from base.views import home
from orders.views import AddCompanyOrder,UpdateCompanyOrder,CompanyOrderDetails, ViewCompanyOrder,AddIndivdualOrder,ViewIndividualOrder,IndividualOrderDetails,UpdateIndividualOrder
from account.views import Registration, UpdateUser, UserRegistry, UserDetails, Login
from trips.views import CompanyTripForm,IndividualTripForm, IndividualTripView, CompanyTripView
from trucks.views import AddTruck,UpdateTruck
from drivers.views import AddDriver,ViewDriver,DriverDetails,UpdateDriver,DeleteDriver
