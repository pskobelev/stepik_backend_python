from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('home', views.index, name='home'),
    path('add_word/', views.add_word, name='add_word'),
    path('add_word', views.add_word, name='add_word'),
    path('words_list/', views.list_words, name='words_list'),
    path('words_list', views.list_words, name='words_list'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
