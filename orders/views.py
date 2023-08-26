from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
# Create your views here.

@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def AddCompanyOrder(request):
    title = "Add Order"
    form = CompanyCreateOrder(request.POST or None)
    queryset = OrderCompany.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New Order added")
            return redirect("orders:viewcompanyorder")
    context = {"companyorder": form, "allorders": queryset, "title": title}
    return render(request, "forms/companyorderform.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
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


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def CompanyOrderDetails(request, pk):
    title = "Order Details"
    queryset = OrderCompany.objects.get(id=pk)
    
    context = {"orderdetails": queryset, "title": title}
    return render(request, "reports/companyorderdetail.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def UpdateCompanyOrder(request, pk):
    title = "Update Order"
    query = OrderCompany.objects.get(id=pk)
    update = CompanyUpdateOrder(request.POST or None, instance=query)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            return redirect("orders:companyorderdetail", pk=pk)
    context = {"updateorder": update, "title": title}
    return render(request, "update/individualdetails.html", context)


# A form to display individual order
@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def AddIndivdualOrder(request):
    title = "Add Order"
    form = IndividualCreateOrder(request.POST or None)
    queryset = OrderIndividual.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New Order added")
        return redirect("orders:viewindividualorder")
    context = {"individualorder": form, "allorders": queryset, "title": title}
    return render(request, "forms/individualorderform.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
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


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def IndividualOrderDetails(request, pk):
    title = "Order Details"
    queryset = OrderIndividual.objects.get(id=pk)

    context = {"orderdetails": queryset, "title": title}
    return render(request, "reports/individualorderdetail.html", context)


@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def UpdateIndividualOrder(request,pk):
    title = "Update Order"
    queryset = OrderIndividual.objects.get(id=pk)
    update = IndividualUpdateOrder(request.POST or None, instance=queryset)
    if request.method == "POST":
        if update.is_valid():
            update.save()
            messages.success(request, "Order Updated")
            return redirect("orders:individualorderdetail", pk=pk)
    context = {"updateorder": update, "title": title}
    return render(request, "update/individualdetails.html", context)

@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def DeleteIOrder(request,pk):
    title = "Delete Order"
    queryset = OrderIndividual.objects.get(id=pk)
    delete = IndividualUpdateOrder(request.POST or None, instance=queryset)
    tag = f"Are you sure you want to delete order for {queryset.fullname} ?"
    if request.method == "POST":
        if delete.is_valid():
            delete.save()
            messages.success(request, "Successfully Deleted")
            return redirect("orders:viewcompanyorder", pk=pk)
    context = {"updateorder": delete, "title": title,"tags":tag}
    return render(request, "delete/deleteiorder.html", context)

@login_required(login_url="account:login")
@staff_member_required(login_url="base:index")
def DeleteCOrder(request,pk):
    title = "Delete Order"
    queryset = OrderCompany.objects.get(id=pk)
    delete = CompanyUpdateOrder(request.POST or None, instance=queryset)
    tag = f"Are you sure you want to delete order for {queryset.company_name} ?"
    if request.method == "POST":
        if delete.is_valid():
            delete.save()
            messages.success(request, "Successfully Deleted")
            return redirect("orders:viewindividualorder")
    context = {"updateorder": delete, "title": title, "tags":tag}
    return render(request,"delete/deletecorder.html", context)

