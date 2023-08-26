from django.urls import path
from . import views
app_name = "drivers"
urlpatterns = [
     path('add-driver/', views.AddDriver, name='driver'),
    path('update-driver/<str:pk>/', views.UpdateDriver, name='updatedriver'),
    path('delete-driver/<str:delete>/', views.DeleteDriver, name='deletedriver'),
    path('showdrivers/', views.ViewDriver, name='displaydriver'),
    path('driverdetails/<str:pk>/', views.DriverDetails, name='driverdetails'),
]