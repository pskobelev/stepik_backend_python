from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dictionary.urls")),
    path("", include("fuelcalc.urls")),
    path("", include("notes.urls")),
    path("", include("online_market.urls")),
]
