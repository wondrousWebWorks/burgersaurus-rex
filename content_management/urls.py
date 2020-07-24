from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_management, name='content-management'),
    path('get-theme/', views.get_theme, name='get-theme'),
]