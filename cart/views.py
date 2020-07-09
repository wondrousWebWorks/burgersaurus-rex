from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages

from menu.models import Product
import json

def view_cart(request):
    """ Renders the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a specified quantity of a given product to the shopping cart """

    try:
        request_body = json.loads(request.body)
        quantity = int(request_body['quantity'])
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to cart.')

        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Something went wrong: {e}')
        return HttpResponse(status=500)


def update_cart(request, item_id):
    """Adjust the quantity of the specified item to what is specified"""

    if request.method == 'POST':
        try:
            request_body = json.loads(request.body)
            quantity = int(request_body['quantity'])
            product = get_object_or_404(Product, pk=item_id)
            cart = request.session.get('cart', {})

            if quantity > 0:
                cart[item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}.')
            else:
                cart.pop(item_id)
                messages.success(request, f'Removed {product.name} from cart.')

            request.session['cart'] = cart
            return HttpResponse(status=200)

        except Exception as e:
            messages.error(request, f'Something went wrong: {e}')
            return HttpResponse(status=500)


def remove_item_from_cart(request, item_id):
    """Remove item from cart"""

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        product = get_object_or_404(Product, pk=item_id)
        messages.success(request, f'Removed {product.name} from cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Something went wrong: {e}')
        return HttpResponse(status=500)