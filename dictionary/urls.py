from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.index, name='home'),
    path('add_word/', views.add_word, name='add_word'),
    path('add_word', views.add_word, name='add_word'),
    path('words_list/', views.list_words, name='words_list'),
    path('words_list', views.list_words, name='words_list'),
]
