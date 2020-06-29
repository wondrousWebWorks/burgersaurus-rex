from django.shortcuts import render

def view_cart(request):
    """ Renders the shopping cart page """

    return render(request, 'cart/cart.html')