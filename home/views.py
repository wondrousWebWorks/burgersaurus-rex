from django.shortcuts import render

from images.models import Image, Page

def home(request):
    """ A view which return the index page """
    images = Image.objects.all()

    carousel_image_1 = images.filter(image_name__icontains='carousel-image-1')[0]
    carousel_image_2 = images.filter(image_name__icontains='carousel-image-2')[0]
    carousel_image_3 = images.filter(image_name__icontains='carousel-image-3')[0]

    context = {
        'carousel_image_1': carousel_image_1,
        'carousel_image_2': carousel_image_2,
        'carousel_image_3': carousel_image_3,
    }

    return render(request, 'home/index.html', context)

