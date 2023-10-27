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
    path('add_fuel', views.add_fuel, name='add_fuel'),
    path('add_fuel/', views.add_fuel, name='add_fuel'),
    path('success', views.success_page, name='success'),
    path('success/', views.success_page, name='success'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
