from django.contrib import admin
from .models import Category, Allergen, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_vegetarian',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class AllergenAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Allergen, AllergenAdmin)
admin.site.register(Product, ProductAdmin)
