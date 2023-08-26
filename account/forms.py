from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    is_staff = forms.BooleanField(label="Give user staff permissions", required=False)
  

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
            "is_active"
        
        ]


# added UserChangeForm by importing from django.contrib.auth.forms
# aslo used the get_user_model() instead of the User by importing from django.contrib.auth import get_user_model()
class UpdateUserForm(UserChangeForm):
    is_staff = forms.BooleanField(label="Give user staff permissions", required=False)
  

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active"
        ]
        # exclude = ["password1", "password2"]
