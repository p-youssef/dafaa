from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('edit_packaging_group/<int:group_id>/',edit_packaging_group,   name='edit_packaging_group'),
    path('add_packaging_group/',                add_packaging_group,    name='add_packaging_group'),

    path('edit_package_s2i/<int:package_id>/',  edit_package_s2i,       name='edit_package_s2i'),
    path('add_package_s2i/',                    add_package_s2i,        name='add_package_s2i'),
    
]

