from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Product, Category
from .forms import ProductForm

def menu(request):

    menu = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu = menu.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'menu': menu,
        'categories': categories
    }

    return render(request, 'menu/menu.html', context)


def add_product(request):
    """Add a product to the store"""

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'menu/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product on the menu """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('menu'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'menu/edit-product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
