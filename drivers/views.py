from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from orders.models import *
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from account.decorators import admin_required

# Create your views here.


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
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
                return redirect("drivers:driver")
            else:
                form.save()
                messages.success(request, "This Driver add successfully")
                return redirect("drivers:displaydriver")
    context = {"driverform": form, "title": title}
    return render(request, "forms/driver_form.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def ViewDriver(request):
    title = "View Driver"
    param_value = request.GET.get("param_name")
    queryset = DriverInfo.objects.all().order_by("id")
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    serial_numbers = list(
        range(
            (page.number - 1) * page.paginator.per_page + 1,
            min(page.number * page.paginator.per_page, page.paginator.count) + 1,
        )
    )

    # Combine serial numbers and items into a list of tuples
    items_with_serial_numbers = zip(serial_numbers, page)

    context = {
        "alldriver": queryset,
        "title": title,
        "page": page,
        "items": items_with_serial_numbers,
    }
    return render(request, "display/driver.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def DriverDetails(request, pk):
    title = "Driver Details"
    unique = DriverInfo.objects.get(id=pk)

    context = {"details": unique, "title": title}
    return render(request, "display/driverdetails.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def UpdateDriver(request, pk):
    title = "Update Driver"
    queryset = DriverInfo.objects.all()
    query = DriverInfo.objects.get(id=pk)
    update = DriverUpdate(request.POST or None, request.FILES or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            messages.success(request, "Update successful")
            return redirect("drivers:driverdetails", pk=pk)
    context = {"updatedriver": update, "title": title}
    return render(request, "update/driverdetails.html", context)


# handle foreignkey that is protected
@admin_required
def DeleteDriver(request, delete):
    title = "Delete Driver"
    try:
        tag = "Are you sure you want to delete this entry ?"
        query = DriverInfo.objects.get(id=delete)
        if request.method == "POST":
            query.delete()
            messages.success(request, "Successfully Deleted")
            return redirect("drivers:displaydriver")
        context = {"tags": tag, "title": title}
        return render(request, "delete/driverdelete.html", context)

    except ProtectedError as e:
        protected_references = []
        for i in e.protected_objects:
            if isinstance(i, OrderCompany):
                protected_references.append(f"{i.trip_no}")
        error_message = (
            f"This driver can't be deleted as he is used in a particular Order: "
            + ", ".join(protected_references)
        )
        context = {"msg": error_message}
        return render(request, "display/drivererror.html", context)
