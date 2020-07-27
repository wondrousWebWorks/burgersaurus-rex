from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Image, Page
from .forms import ImageForm

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
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully changed image!')
            return redirect('images')
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:        
        form = ImageForm(instance=image)
        messages.info(request, f'You are editing {image.image_friendly_name}')

    template = 'images/edit-image.html'
    context = {
        'image': image,
        'form': form,
    }

    return render(request, template, context)
