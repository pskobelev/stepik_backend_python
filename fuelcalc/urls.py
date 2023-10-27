from django.urls import path

from . import views

urlpatterns = [
    path('add_fuel', views.add_fuel, name='add_fuel'),
    path('add_fuel/', views.add_fuel, name='add_fuel'),
]
