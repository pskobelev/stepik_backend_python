from django.shortcuts import render, redirect

DBFILE = './words_list.txt'


def index(request):
    """Index page"""
    return render(request, 'index.html')


def add_word(request):
    """Func add words to the list of words"""
    if request.method == 'POST':
        _object = request.POST
        add_to_file(_object)
        return redirect(index)
    return render(request, 'add_words.html')


def add_to_file(_object):
    """write data to file"""
    with open(DBFILE, 'a+', encoding='UTF-8') as f:
        key = _object['word1']
        value = _object['word2']
        f.write(f'{key} - {value}\n')


def read_from_file():
    """read from file"""
    file = open(DBFILE, 'r+', encoding='UTF-8').read().splitlines()
    words1, words2 = [], []
    for line in file:
        word1, word2 = line.split('-')
        words1.append(word1)
        words2.append(word2)
    return words1, words2


def list_words(request):
    """returns a list of words"""
    data = read_from_file()
    words = {key.strip(): value.strip() for key, value in zip(data[0], data[1])}
    return render(request,
                  'words_list.html',
                  {'words': words})
