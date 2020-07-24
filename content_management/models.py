from colorfield.fields import ColorField
from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    colour_1 = ColorField(default='#FF0000', null=False, blank=False)
    colour_2 = ColorField(default='#FFFF00', null=False, blank=False)
    colour_3 = ColorField(default='#00FF00', null=False, blank=False)
    colour_4 = ColorField(default='#FF00FF', null=False, blank=False)
    colour_5 = ColorField(default='#0000FF', null=False, blank=False)
    dark_mode_background_colour = ColorField(default='#1c1c1c', null=False, blank=False)

    def __str__(self):
        return self.name