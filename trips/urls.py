from django.urls import path
from . import views

app_name = "trips"

urlpatterns = [
    path("add-Itrip/", views.IndividualTripForm, name="individualtrip"),
    path("view-Itrip/", views.IndividualTripView, name="viewindividualtrip"),
    path("update-Itrip/<str:pk>/", views.ITripUpdate, name="updateindividualtrip"),
    path("delete-Itrip/<str:pk>/", views.DeleteItrip, name="deleteindividualtrip"),
    path("update-Ctrip/<str:pk>/", views.CTripUpdate, name="updatecompanytrip"),
    path("add-Ctrip/", views.CompanyTripForm, name="companytrip"),
    path("view-Ctrip/", views.CompanyTripView, name="viewcompanytrip"),
    path("delete-Ctrip/<str:pk>/", views.DeleteCtrip, name="deletecompanytrip"),
    path('view-trip-corders/<str:ctrip>/', views.ctrip_order, name='ctorders'),
    path('view-trip-iorders/<str:itrip>/', views.itrip_order, name='itorders'),
    path('print-corders/<str:cprint>/', views.print_ctrip_order, name='cprint'),
    path('print-iorders/<str:iprint>/', views.print_itrip_order, name='iprint'),
    
]
