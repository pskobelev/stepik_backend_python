from django.urls import path

from notes import views

urlpatterns = [
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("reg/", views.sign_up, name="signup"),
    path("notes/", views.list_notes, name="notes_list"),
    path("add_note/", views.add_note, name="add_note"),
]
