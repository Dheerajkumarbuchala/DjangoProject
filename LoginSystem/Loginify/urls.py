from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path("hello_world/", views.hello_world),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
]