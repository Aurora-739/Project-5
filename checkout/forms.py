# checkout/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    save_info = forms.BooleanField(required=False, label='Save this information to my profile')

    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'address_line1',
            'address_line2',
            'postcode',
            'city',
            'country',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'postcode': 'Postcode',
            'city': 'City',
            'country': 'Country',
        }
        for field_name, placeholder in placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].label = False
