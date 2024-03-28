from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from orders.models import OrderCompany, OrderIndividual
from .forms import *
from orders.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.deletion import ProtectedError


# Create your views here.
@login_required(login_url="account:login")
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


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def IndividualTripView(request):
    title = "Trips"
    query = IndividualTrips.objects.all()

    context = {"title": title, "iadded": query}
    return render(request, "display/itrip.html", context)



@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def ITripUpdate(request, pk):
    title = "Update Trips"
    query = IndividualTrips.objects.get(id=pk)
    update = IndividualUpdateTrips(request.POST or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            return redirect("trips:viewindividualtrip")
        
    context = {"title": title, "trip": update}
    return render(request, "update/itrip.html", context)


def DeleteItrip(request, pk):
    title = "Delete Individual Trip"
    try:
        query = get_object_or_404(IndividualTrips, id=pk)
        tag = f"Are you sure you want to delete this trip: {query.name}/{query.id}/{query.initials}/{query.date} ?"
        if request.method == "POST":
            query.delete()
            messages.success(request,"Trip Successfully Deleted")
            return redirect("trips:viewindividualtrip")
        
        context = {"title": title, "trip": query, "tags":tag}
        return render(request, "delete/itrip.html", context)
    except ProtectedError as e:
        protected_references = []
        for i in e.protected_objects:
            if isinstance(i, OrderIndividual):
                protected_references.append(f'{i.trip_no}')
        error_message = f"This Trip can not be deleted as it is used in a particular Company Order: " + ". ".join(protected_references)
        context = {
            "msg":error_message
        }
        return render(request, 'delete/itriperror.html', context)

@login_required(login_url="account:login")
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


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def CompanyTripView(request):
    title = "Trips"
    queryset = CompanyTrips.objects.all()

    context = {"title": title, "added": queryset}
    return render(request, "display/ctrip.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def CTripUpdate(request, pk):
    title = "Update Trips"
    query = CompanyTrips.objects.get(id=pk)
    update = CompanyUpdateTrips(request.POST or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            messages.success(request,"Trip Successfully Updated")
            return redirect("trips:viewcompanytrip")
        
    context = {"title": title, "trip": update}
    return render(request, "update/ctrip.html", context)


def DeleteCtrip(request, pk):
    title = "Delete Company Trip"
    try:
        query = get_object_or_404(CompanyTrips, id=pk)
        tag = f"Are you sure you want to delete this trip: {query.name}/{query.id}/{query.initials}/{query.date} ?"
        if request.method == "POST":
            query.delete()
            messages.success(request,"Trip Successfully Deleted")
            return redirect("trips:viewcompanytrip")
        
        context = {"title": title, "trip": query, "tags":tag}
        return render(request, "delete/ctrip.html", context)
    except ProtectedError as e:
        protected_references = []
        for i in e.protected_objects:
            if isinstance(i, OrderCompany):
                protected_references.append(f'{i.trip_no}')
        error_message = f"This Trip can not be deleted as it is used in a particular Company Order: " + ". ".join(protected_references)
        context = {
            "msg":error_message
        }
        return render(request, 'delete/ctriperror.html', context)


def ctrip_order(request, ctrip):
    ctrip = get_object_or_404(CompanyTrips, id=ctrip)
    corder = OrderCompany.objects.filter(trip_no=ctrip)
    context ={
        'ctrip':ctrip,
        'corder':corder
    }
    return render(request, "display/viewordertrips.html", context)


def print_ctrip_order(request, cprint):
    corder = get_object_or_404(OrderCompany, id=cprint)
    context ={
        'corder':corder
    }
    return render(request, "print/cprint.html", context)


def itrip_order(request, itrip):
    itrip = get_object_or_404(IndividualTrips, id=itrip)
    iorder = OrderIndividual.objects.filter(trip_no=itrip)
    context ={
        'itrip':itrip,
        'iorder':iorder
    }
    return render(request, "display/iviewordertrips.html", context)

def print_itrip_order(request, iprint):
    iorder = get_object_or_404(OrderIndividual, id=iprint)
    context ={
        'iorder':iorder
    }
    return render(request, "print/iprint.html", context)