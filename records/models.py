from django.db import models

"""
a class represent a selling record

Attributes
----------
+ item: Product_Item
+ selling_date: date

Methods
-------

"""
class Selling_Record(models.Model):
    from production.models import Product_Item


    item            = models.ForeignKey(Product_Item, related_name='item', on_delete=models.CASCADE, blank=True, null=True)
    selling_date    = models.DateField()
    price           = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return str(self.price)
