from django.urls import path
from . import views
app_name="trucks"
urlpatterns = [
    path('add-truck/', views.AddTruck, name='truck'),
    path('update-truck/<str:pk>/', views.UpdateTruck, name='updatetruck'),
    path('delete-truck/<str:delete>/', views.DeleteTruck, name='deletetruck'),
]