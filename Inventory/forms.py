# from django.forms import ModelForm
from django import forms
from .models import *

class Product_Form(forms.ModelForm):

    class Meta:

        model = Product
        fields = '__all__'

        widgets = {
            'product_name' : forms.TextInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'product_code' : forms.TextInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'price' :  forms.NumberInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'gst' :  forms.NumberInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'picture' :  forms.FileInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
        }