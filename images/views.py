from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from images.models import Image, Page

def images(request):
    """Renders all image entries in the Image model"""
    images = Image.objects.all()

    template = 'images/images.html'
    context = {
        'images': images,
    }

    return render(request, template, context)

@login_required
def edit_image(request, image_id):
    """ Edit an image """
    if not request.user.is_superuser:
        messages.info(request, 'Oops! You don\'t have the required permission to access this page. Login with the required credentials to do so!')
        return redirect(reverse('home'))

    image = get_object_or_404(Image, pk=image_id)

    template = 'images/edit-image.html'
    context = {
        'image': image,
    }

    return render(request, template, context)
