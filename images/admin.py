from django.contrib import admin
from .models import Page, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'page',
        'image_name',
        'image',
    )

admin.site.register(Page)
admin.site.register(Image, ImageAdmin)
