from django.shortcuts import render, redirect
from trucks.models import *
from orders.models import *
from trips.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='account:login')
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