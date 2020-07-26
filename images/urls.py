from django.urls import path
from . import views

urlpatterns = [
    path('', views.images, name='images'),
    path('edit-image/<int:image_id>', views.edit_image, name='edit-image'),
]