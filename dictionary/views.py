from django.shortcuts import render, redirect

from dictionary.models import Words, Fuel


def index(request):
    """Index page"""
    return render(request, 'index.html')


def success_page(request):
    return render(request, 'success.html')


def add_word(request):
    """Func add words to the list of words"""
    if request.method == 'POST':
        _object = request.POST
        if Words.objects.filter(word=_object['word']).exists():
            pass
        else:
            new_word = Words(word=_object['word'], description=_object['description'])
            new_word.save()
            return redirect(index)
    return render(request, 'add_words.html')


def list_words(request):
    """returns a list of words"""
    data = Words.objects.all().order_by('-id')
    return render(request,
                  'words_list.html',
                  {'words': data})


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
    else:
        history = fuel_history()
        return render(request, 'add_fuel.html', context={'history': history})


def calculate_liters_per_100km(fuel, distance):
    """fuel_consumption"""
    return round((int(fuel) / int(distance)) * 100, 2)


def fuel_history():
    """fuel_history"""
    data = Fuel.objects.all().order_by('-date_fuel')
    return data
