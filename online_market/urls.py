from django.urls import path, re_path

from online_market import views

urlpatterns = [
    path("get_token", views.get_token, name="get_token"),
    re_path(r"goods/?$", views.GoodsAPI.as_view()),
    re_path(r"new_good/?$", views.GoodsAPI.as_view()),
]
