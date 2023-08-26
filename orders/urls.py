from django.urls import path
from . import views

app_name="orders"
urlpatterns=[

    path('addcompanyorder/', views.AddCompanyOrder, name='companyorder'),
    path('update-companyorder/<str:pk>/', views.UpdateCompanyOrder, name='updatecompanyorder'),
    path('viewcompanyorder/', views.ViewCompanyOrder, name='viewcompanyorder'),
    path('companyorderdetails/<str:pk>/', views.CompanyOrderDetails, name='companyorderdetail'),
    path('addindividualorder/', views.AddIndivdualOrder, name='individualorder'),
    path('update-individualorder/<str:pk>/', views.UpdateIndividualOrder, name='updateindividualorder'),
    path('viewindividualorder/', views.ViewIndividualOrder, name='viewindividualorder'),
    path('individualorderdetails/<str:pk>/', views.IndividualOrderDetails, name='individualorderdetail'),
    path('idelete/<str:pk>/', views.DeleteIOrder, name='idelete'),
    path('cdelete/<str:pk>/', views.DeleteCOrder, name='cdelete'),
]