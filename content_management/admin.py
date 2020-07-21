from content_management.models import Theme
from django.contrib import admin

from .models import Theme

class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'colour_1',
        'colour_2',
        'colour_3',
        'colour_4',
        'colour_5',
    )

admin.site.register(Theme, ThemeAdmin)
