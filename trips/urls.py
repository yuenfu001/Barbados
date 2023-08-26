from django.urls import path
from . import views

app_name = "trips"

urlpatterns = [
    path("add-Itrip/", views.IndividualTripForm, name="individualtrip"),
    path("view-Itrip/", views.IndividualTripView, name="viewindividualtrip"),
    # path("update-Itrip/<str:update>/", views.ITripUpdate, name="updateindividualtrip"),
    path("add-Ctrip/", views.CompanyTripForm, name="companytrip"),
    path("view-Ctrip/", views.CompanyTripView, name="viewcompanytrip"),
]
