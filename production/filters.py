# filters.py
import django_filters
from .models import *

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Product_Item
        fields = {
            'name': ['icontains'],
            'product': ['exact'],
            'first_offer_price': ['lt', 'gt'],
            'selled': ['exact'],
            'creater': ['exact'],
        }
