from django.urls import path

from . import views

urlpatterns = [
    path("add_fuel", views.add_fuel, name="add_fuel"),
    path("add_fuel/", views.add_fuel, name="add_fuel"),
    path("add_fuel2", views.add_fuel_over_forms, name="add_fuel2"),
]
