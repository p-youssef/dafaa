# accounts/forms.py
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','default_weight','default_width','default_height','default_length', 'description']


class ProductItemForm(forms.ModelForm):
    class Meta:
        model = Product_Item
        fields = ['name','product','Weight','width','height','length','description','packaging_group','raw_material_value','online_shop','preducing_date','first_offer_price','creater']



class ProductItemImageForm(forms.ModelForm):
    class Meta:
        model = Product_Item_Image
        fields = ['item','image','description']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Product_Category
        fields = ['name','description']

