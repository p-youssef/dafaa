from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('dashboard/',                      production_dashboard,       name='production_dashboard'),

    path('products_management_view/',       products_management_view,   name='products_management_view'),
    path('categories_management_view/',     categories_management_view, name='categories_management_view'),

    path('add_product/',                    add_product,                name='add_product'),
    path('edit_product/<int:product_id>/',  edit_product,               name='edit_product'),

    path('add_item/<int:product_id>/',      add_item,                   name='add_item'),
    path('edit_item/<int:item_id>/',        edit_item,                  name='edit_item'),

    path('add_category/',                   add_category,               name='add_category'),
    path('edit_category/<int:category_id>/',edit_category,              name='edit_category'),
    
]

