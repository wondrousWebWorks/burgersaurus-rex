from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Image(models.Model):
    page = models.ForeignKey('Page', null=True, blank=True, on_delete=models.SET_NULL)
    image_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=False)
