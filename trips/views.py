from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required(login_url='account:login')
@staff_member_required(login_url="base:index")
def IndividualTripForm(request):
    title = "Trips"
    query = IndividualTrips.objects.all()
    iform = IndividualCreateTrips(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if iform.is_valid():
            initials = iform.cleaned_data["initials"]
            if query.filter(initials=initials).exists():
                messages.error(request, "This Trip Name already exists")
                return redirect("trips:individualtrip")
            else:
                iform.save()
                messages.success(request, "New Trip added successfully")
                return redirect("trips:viewindividualtrip")
    context = {"itrip": iform, "title": title, "iadded": query}
    return render(request, "forms/itrip.html", context)


@login_required(login_url='account:login')
@staff_member_required(login_url="base:index")
def IndividualTripView(request):
    title = "Trips"
    query = IndividualTrips.objects.all()
    
   
    context = {"title": title, "iadded": query}
    return render(request, "display/itrip.html", context)


@login_required(login_url='account:login')
@staff_member_required(login_url="base:index")
def CTripUpdate(request):
    title = "Update Trips"
    query = CompanyTrips.objects.all()
   
    context = {"title": title, "iadded": query}
    return render(request, "display/itrip.html", context)


@login_required(login_url='account:login')
@staff_member_required(login_url="base:index")
def CompanyTripForm(request):
    title = "Trips"
    queryset = CompanyTrips.objects.all()
    form = CompanyCreateTrips(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            initials = form.cleaned_data["initials"]
            if queryset.filter(initials=initials).exists():
                messages.error(request, "This Trip Name already exists")
                return redirect("trips:companytrip")
            else:
                form.save()
                messages.success(request, "New Trip added successfully")
                return redirect("trips:viewcompanytrip")
    context = {"trip": form, "title": title, "added": queryset}
    return render(request, "forms/ctrips.html", context)



@login_required(login_url='account:login')
@staff_member_required(login_url="base:index")
def CompanyTripView(request):
    title = "Trips"
    queryset = CompanyTrips.objects.all()
   
    context = {"title": title, "added": queryset}
    return render(request, "display/ctrip.html", context)

