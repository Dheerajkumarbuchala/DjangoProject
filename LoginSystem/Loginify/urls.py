from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path("hello_world/", views.hello_world),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('users/', views.get_all_users_view, name='all_users'),
    path('user/<str:email>/', views.get_user_by_email_view, name='user_detail'),
    path('user/update/<str:email>/', views.update_user_view, name='update_user'),
    path('user/delete/<str:email>/', views.delete_user_view, name='delete_user'),
]