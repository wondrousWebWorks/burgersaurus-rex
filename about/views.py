from django.shortcuts import render

from images.models import Image


def about(request):
    """Returns a rendered template of the about page"""
    images = Image.objects.all()

    about_header = images.filter(image_name__icontains='about-header')[0]
    about_farm = images.filter(image_name__icontains='about-farm')[0]
    about_hydroponics = images.filter(image_name__icontains='about-hydroponics')[0]

    template = 'about/about.html'

    context = {
        'about_header': about_header,
        'about_farm': about_farm,
        'about_hydroponics': about_hydroponics,
    }

    return render(request, template, context)
