from django.shortcuts import render, redirect

from dictionary.models import Words


def index(request):
    """Index page"""
    return render(request, 'index.html')


def add_word(request):
    """Func add words to the list of words"""
    if request.method == 'POST':
        _object = request.POST
        new_word = Words(word=_object['word'], description=_object['description'])
        new_word.save()
        return redirect(index)
    return render(request, 'add_words.html')


def list_words(request):
    """returns a list of words"""
    data = Words.objects.all()
    return render(request,
                  'words_list.html',
                  {'words': data})
