from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path("hello_world/", views.hello_world),
]