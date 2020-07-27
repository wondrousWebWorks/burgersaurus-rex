from django import forms
from .models import Image, Page


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = 'image',

    image = forms.ImageField(label='Image', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)