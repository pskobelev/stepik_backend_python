from django.shortcuts import render, redirect

from dictionary.views import success_page
from fuelcalc.models import Fuel


# Create your views here.
def add_fuel(request):
    """Write data to database"""
    if request.method == 'POST':
        fuel = request.POST.get('fuel')
        cost = request.POST.get('cost')
        distance = request.POST.get('distance')
        fuel_consumption = calculate_liters_per_100km(fuel, distance)
        data = Fuel(fuel=int(fuel), cost=int(cost), distance=int(distance), fuel_consumption=fuel_consumption)
        data.save()

        return redirect(success_page)

    history = fuel_history()
    return render(request, 'add_fuel.html', context={'history': history})


def calculate_liters_per_100km(fuel: int, distance: int) -> float:
    """fuel_consumption"""
    return round((int(fuel) / int(distance)) * 100, 2)


def fuel_history():
    """fuel_history"""
    data = Fuel.objects.all().order_by('-date_fuel')
    return data
