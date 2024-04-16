import re

from django.forms import ModelForm, forms
from django.views.generic import FormView

from apps.models import Product, Order


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        exclude = ()


class ProductOrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'phone_number', 'product')

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^\+998\(\d{2}\) \d{3}-\d{2}-\d{2}$', phone_number):
            raise forms.ValidationError("Invalid phone number format. Please use the format +998(__) ___-__-__")
        return phone_number
