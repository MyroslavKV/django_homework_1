from django.contrib import admin
from django.urls import path
from .views import language_list

app_name = "blog"

urlpatterns = [
    path("language/", language_list, name="language"),
]