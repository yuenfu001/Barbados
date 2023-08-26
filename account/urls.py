from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "account"
urlpatterns = [
    path('register/', views.Registration, name='register'),
    path('update-user/<str:pk>/', views.UpdateUser, name='updateuser'),
    path('registry/', views.UserRegistry, name='registry'),
    path('user-details/<str:pk>/', views.UserDetails, name='userdetails'),
    path('login/', CreateLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-user/<str:pk>/', views.DeleteUser, name='deleteuser'),
]