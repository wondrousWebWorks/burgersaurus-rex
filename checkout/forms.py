from django import forms
from .models import Order

CITIES = [
    ('cork', 'Cork'),
    ('dublin', 'Dublin'),
    ('galway', 'Galway'),
    ('limerick', 'Limerick'),
    ('waterford', 'Waterford')
]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, set autofocus on first field and remove labels 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        self.fields['town_or_city'] = forms.Charfield(widget=forms.Select(choices=CITIES))
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'* {placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholder
            