from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import *
from .decorators import *
# Create your views here.



class CreateLoginView(LoginView):
    template_name = "authentications/login.html"
    authentication_form = LoginForm

@admin_required
def Registration(request):
    register = RegisterForm(request.POST or None)
    if request.method == "POST":
        if register.is_valid():
            register.save()
            messages.success(request,"User successfully added")
            return redirect("account:registry")
    context = {
            "register":register
    }
    return render(request, "authentications/register.html", context)


# used the get_user_model from the django.contrib.auth import get_user_model in the forms.py
@admin_required
def UpdateUser(request, pk):
    User = get_user_model()
    user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateUserForm(request.POST or None, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request,"User successfully updated")
            return redirect("account:userdetails", pk=pk)
    
    else:
        form = UpdateUserForm(instance=user)
        
    context = {
            "updateuser":form, "user":user
    }
    return render(request, "authentications/updateuser.html", context)

@admin_required
def UserRegistry(request):
    viewuser = User.objects.all()
    context = {
            "registry":viewuser
    }
    return render(request, "display/viewregistry.html", context)

@admin_required
def UserDetails(request, pk):
    details = User.objects.get(id=pk)
    context = {
            "details":details
    }
    return render(request, "display/userdetails.html", context)

def DeleteUser(request, pk):
    title = "Delete Ueer"
    user = get_object_or_404(User, id=pk)
    tag = f"Are you sure you want to delete this user: {user.username} ?"
    if request.method == "POST":
            user.delete()
            messages.success(request,"Successfully Deleted")
            return redirect("account:registry")
    
    context ={
                "tags":tag, "title":title, "user":user
        }
    return render(request, "delete/deleteuser.html", context)

