from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    colour_1 = models.CharField(max_length=6, null=False, blank=False)
    colour_2 = models.CharField(max_length=6, null=False, blank=False)
    colour_3 = models.CharField(max_length=6, null=False, blank=False)
    colour_4 = models.CharField(max_length=6, null=False, blank=False)
    colour_5 = models.CharField(max_length=6, null=False, blank=False)
    dark_mode_background_colour = models.CharField(max_length=6, null=False, blank=False, default='1c1c1c')

    def __str__(self):
        return self.name