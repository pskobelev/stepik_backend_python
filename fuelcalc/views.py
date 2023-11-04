from django.shortcuts import render, redirect

from dictionary.views import success_page
from fuelcalc.models import Fuel, MyFuelForm


# Create your views here.
def add_fuel(request):
    """Write data to database"""
    if request.method == "POST":
        fuel = request.POST.get("fuel")
        cost = request.POST.get("cost")
        distance = request.POST.get("distance")
        fuel_consumption = calculate_liters_per_100km(fuel, distance)
        data = Fuel(
            fuel=int(fuel),
            cost=int(cost),
            distance=int(distance),
            fuel_consumption=fuel_consumption,
        )
        data.save()

        return redirect(success_page)

    queryset = Fuel.objects.all().order_by("-date_fuel")
    context = {"history": queryset}
    return render(request, "add_fuel.html", context=context)


def calculate_liters_per_100km(fuel: int, distance: int) -> float:
    """fuel_consumption"""
    return round((int(fuel) / int(distance)) * 100, 2)


def add_fuel_over_forms(request):
    """add fuel"""
    if request.method == "POST":
        form = MyFuelForm(request.POST)
        if form.is_valid():
            fuel = form.save(commit=False)
            fuel.fuel_consumption = calculate_liters_per_100km(
                int(form.cleaned_data["fuel"]), form.cleaned_data["distance"]
            )
            fuel.save()
            return redirect("success")
    else:
        form = MyFuelForm()
    queryset = Fuel.objects.all().order_by("-date_fuel")
    return render(request, "form.html", {"form": form, "history": queryset})
