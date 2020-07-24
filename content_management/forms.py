from django import forms
from .models import Theme

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme

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

        colour_1 = forms.CharField(widget=ColorPickerWidget)
        colour_2 = forms.CharField(widget=ColorPickerWidget)
        colour_3 = forms.CharField(widget=ColorPickerWidget)
        colour_4 = forms.CharField(widget=ColorPickerWidget)
        colour_5 = forms.CharField(widget=ColorPickerWidget)
        dark_mode_background_colour = forms.CharField(widget=ColorPickerWidget)

        self.fields['colour_1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'* {placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False
        self.fields[field].widget.attrs['class'] = 'profile-form-input'