from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    colour_1 = models.CharField(max_length=6, null=False, blank=False)
    colour_2 = models.CharField(max_length=6, null=False, blank=False)
    colour_3 = models.CharField(max_length=6, null=False, blank=False)
    colour_4 = models.CharField(max_length=6, null=False, blank=False)
    colour_5 = models.CharField(max_length=6, null=False, blank=False)

    def __str__(self):
        return self.name