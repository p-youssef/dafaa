from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('all/', users_management_view, name='users_view'),
    path('<int:user_id>/', edit_user, name='user_view'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='custom-login'),
    path('add_user/', add_user, name='add_user'),


]