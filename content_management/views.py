from django.shortcuts import render
from django.http import JsonResponse

from .models import Theme
from .forms import ThemeForm

def content_management(request):

    form = ThemeForm;
    template = 'content_management/content-management.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
