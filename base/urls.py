from django.urls import path
from trips import views
from . import views
app_name="base"
urlpatterns = [
    path('', views.home, name='index'),
]