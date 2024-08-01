from django import forms
from .models import *

class PackagingGroupForm(forms.ModelForm):
    class Meta:
        model = Packaging_Group
        fields = ['name','description','price']



class PackageS2IForm(forms.ModelForm):
    class Meta:
        model = Package_S2I
        fields = ['weight','cost']