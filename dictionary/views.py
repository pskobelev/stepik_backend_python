from django.shortcuts import render, redirect

from dictionary.models import Words


def index(request):
    """Index page"""
    return render(request, "index.html")


def success_page(request):
    return render(request, "success.html")


def add_word(request):
    """Func add words to the list of words"""
    if request.method == "POST":
        _object = request.POST
        if Words.objects.filter(word=_object["word"]).exists():
            # TODO: add message
            pass
        else:
            new_word = Words(
                word=_object["word"], description=_object["description"]
            )
            new_word.save()
            return redirect(index)
    return render(request, "add_words.html")


def list_words(request):
    """returns a list of words"""
    return render(
        request,
        "words_list.html",
        {"words": (Words.objects.all().order_by("-id"))},
    )
