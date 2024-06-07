from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import *
from drivers.models import *
from .forms import *
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from account.decorators import admin_required


# Create your views here.
@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def AddTruck(request):
    title = "Add Truck"
    form = TruckCreate(request.POST or None)
    queryset = TruckInfo.objects.all().order_by("id")
    print("Queryset Length:", len(queryset))
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    serial_numbers = list(range(
        (page.number - 1) * page.paginator.per_page + 1,
        min(page.number * page.paginator.per_page, page.paginator.count) + 1
    ))

    # Combine serial numbers and items into a list of tuples
    items_with_serial_numbers = zip(serial_numbers, page)
    if request.method == "POST":
        if form.is_valid():
            bl_number = form.cleaned_data["bl_number"]
            plates = form.cleaned_data["plate_number"]
            if queryset.filter(bl_number=bl_number, plate_number=plates).exists():
                messages.error(request, "This Truck Number already exist")
                return redirect("trucks:truck")
            else:
                form.save()
            return redirect("trucks:truck")
    context = {
        "truckform": form,
        "alltruck": queryset,
        "title": title,
        "page": page,
        "items": items_with_serial_numbers,
    }
    return render(request, "forms/truckform.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def UpdateTruck(request, pk):
    title = "Update Truck"
    queryset = TruckInfo.objects.get(id=pk)
    update = TruckUpdate(request.POST or None, instance=queryset)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            messages.success(request, "Update Successful")
            return redirect("trucks:truck")
        # else:
        #     messages.error(request, "Update Not Successful")

    context = {"updatetruck": update, "alltruck": queryset, "title": title}
    return render(request, "update/trucks.html", context)


@admin_required
def DeleteTruck(request, delete):
    title = "Delete Truck"
    tag = "Are you sure you want to delete this entry ?"
    queryset = TruckInfo.objects.get(id=delete)
    update = TruckUpdate(request.POST or None, instance=queryset)
    if request.method == "POST":
        queryset.delete()
        messages.success(request, "Successfully Deleted")
        return redirect("trucks:truck")

    context = {"updatetruck": update, "alltruck": queryset, "tags": tag, "title": title}
    return render(request, "delete/deletetruck.html", context)
