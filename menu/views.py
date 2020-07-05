from django.shortcuts import render

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
    """ Add a product to the store """
    form = ProductForm()
    template = 'menu/add-product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
