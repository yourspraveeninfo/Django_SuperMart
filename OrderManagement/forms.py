# from django.forms import ModelForm
from django import forms
from .models import *

class Customer_Form(forms.ModelForm):

    class Meta:

        model = Customer
        fields = '__all__'

        widgets = {
            'customer_name' : forms.TextInput(attrs={'class':"form-control mt-1 mx-2 mb-3 "}),
            'customer_since' :  forms.DateInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
        }

class Orders_Form(forms.ModelForm):

    class Meta:

        model = Orders
        fields = ['customer_reference', 'product_reference', 'order_number', 'order_date', 'quantity']

        widgets = {
            'customer_reference' : forms.Select(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'product_reference' : forms.Select(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'order_number' :  forms.NumberInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'order_date' :  forms.DateInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
            'quantity' :  forms.NumberInput(attrs={'class':"form-control mt-1 mx-2 mb-3"}),
        }