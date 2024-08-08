from django.db import models
import datetime



"""
    class represents packaging group.

    Attributes
    ----------
    + name: str


    Methods
    -------


"""
class Packaging_Group(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name





"""
    class represents a linke betowen packaging group and backaging item.

    Attributes
    ----------
    + send_by: date
    + weight: float
    + cost: float
    + send: bool



    Methods
    -------


"""
class Package_S2I(models.Model):
    send_by     = models.DateField(null=True, blank=True)
    weight      = models.DecimalField(max_digits=10, decimal_places=2)
    cost        = models.DecimalField(max_digits=10, decimal_places=2)
    send        = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Package N."+ str(self.pk)
    
    def set_as_send(self):
        self.send = True
        self.send_by = datetime.date.today()
        self.save()