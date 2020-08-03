from django import forms
from .models import UserProfile

CITIES = [
    ('', 'Select a City'),
    ('Cork', 'Cork'),
    ('Dublin', 'Dublin'),
    ('Galway', 'Galway'),
    ('Limerick', 'Limerick'),
    ('Waterford', 'Waterford')
]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, set autofocus on first field and remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'City',
            'default_postcode': 'Postal Code',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        self.fields['default_town_or_city'] = forms.ChoiceField(choices=CITIES)
        for field in self.fields:
            if field != 'default_town_or_city':
                if self.fields[field].required:
                    placeholder = f'* {placeholders[field]}'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
