from django import forms
from colorfield.fields import ColorField

from .models import Theme

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = (
            'colour_1',
            'colour_2',
            'colour_3',
            'colour_4',
            'colour_5',
            'dark_mode_background_colour',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, set autofocus on first field and remove labels 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'colour_1': 'Colour 1',
            'colour_2': 'Colour 2',
            'colour_3': 'Colour 3',
            'colour_4': 'Colour 4',
            'colour_5': 'Colour 5',
            'dark_mode_background_colour': 'Dark Mode Background Colour',
        }

        colour_1 = ColourField()
        colour_2 = ColourField()
        colour_3 = ColourField()
        colour_4 = ColourField()
        colour_5 = ColourField()
        dark_mode_background_colour = ColourField()

        self.fields['colour_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'* {placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
        self.fields[field].widget.attrs['class'] = 'profile-form-input'