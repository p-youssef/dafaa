from django.db import models
from product_packaging.models import *
from django.contrib.auth.models import User
#from records.models import *
import datetime, os

"""
    A class used to represent a Product Category.

    Attributes
    ----------
    name : CharField
        product name
    description : TextField
        description of the category


    Methods
    -------

"""
class Product_Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name



"""
    A class used to represent a Product.

    Attributes
    ----------
    name : CharField
        product name

    category : ForeignKey <Product_Category>
        product category

    weight : DecimalField
        product weight
        
    width : DecimalField
        product width
    
    height : DecimalField
        product height

    length : DecimalField
        product length


    Methods
    -------

"""
class Product(models.Model):
    
    name                = models.CharField(max_length=100)
    category            = models.ForeignKey(Product_Category, related_name='category', on_delete=models.CASCADE, blank=True, null=True)
    description         = models.TextField()


    default_weight      = models.DecimalField(max_digits=10, decimal_places=2)
    default_width       = models.DecimalField(max_digits=10, decimal_places=2)
    default_height      = models.DecimalField(max_digits=10, decimal_places=2)
    default_length      = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name



"""
    A class used to represent a Product.

    Attributes
    ----------
    + product: Product
    + description: text
    + Weight: float
    + width: float
    + height: float
    + length: float
    + preduced: bool
    + selled: bool
    + Packaging_group: Packaging_Group
    + package_S2I: Package_S2I
    + raw_material_value: float
    + online_shop: dict <shop name: link>
    + preducing_date: date
    + first_offer_price: float
    + creater: user


    Methods
    -------

"""
class Product_Item(models.Model):
    name                = models.CharField(max_length=100)
    product             = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    Weight              = models.DecimalField(max_digits=10, decimal_places=2)
    width               = models.DecimalField(max_digits=10, decimal_places=2)
    height              = models.DecimalField(max_digits=10, decimal_places=2)
    length              = models.DecimalField(max_digits=10, decimal_places=2)
    description         = models.TextField()
    preduced            = models.BooleanField(default = False)
    selled              = models.BooleanField(default = False)
    packaging_group     = models.ForeignKey(Packaging_Group, related_name='packaging_group', on_delete=models.CASCADE, blank=True, null=True)
    package_S2I         = models.ForeignKey(Package_S2I, related_name='package_S2I', on_delete=models.CASCADE, blank=True, null=True) 
    raw_material_value  = models.DecimalField(max_digits=10, decimal_places=2)
    online_shop         = models.JSONField(default = dict)
    preducing_date      = models.DateField()
    first_offer_price   = models.DecimalField(max_digits=10, decimal_places=2)
    creater             = models.ForeignKey(User, related_name='creater', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    def set_as_sold(self, price):
        self.selled = True
        self.save()

        from records.models import Selling_Record

        Selling_Record.objects.create(item = self,selling_date = datetime.date.today(), price = price)

    def set_as_preduced(self):
        self.preduced = True
        self.save()


    def delete_image(request, image_id):
        item_image = Product_Item_Image.objects.get(pk = image_id)
        if os.path.isfile(item_image.image.path):
            os.remove(item_image.image.path)

        item_image.delete()
        





class Product_Item_Image(models.Model):
    
    item        = models.ForeignKey(Product_Item, related_name='images', on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='items/')
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.item) + ' - image N.' + str(self.pk)