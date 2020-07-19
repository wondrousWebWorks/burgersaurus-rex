from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add-product/', views.add_product, name='add-product'),
    path('edit-product/<int:product_id>', views.edit_product, name='edit-product'),
    path('delete-product/<int:product_id>', views.delete_product, name='delete-product')
]
