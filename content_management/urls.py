from django.urls import path
from . import views

urlpatterns = [
    path('get-theme/', views.get_theme, name='get-theme'),
]