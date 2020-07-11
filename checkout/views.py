from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_content
import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect(reverse('menu'))

    current_cart = cart_content(request)
    cart_total = current_cart['order_total']
    stripe_total = round(cart_total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqPsYKP14WGiq4LBCGkpzDps5JORfc9euGYZUeYnUBmby6Uzqcg0KMqQTuNDFw1dOOXHG3h4XH0QBoAeACTd46V00lnRRF4t9',
        'client_secret': 'test-client-secret',
    }

    return render(request, template, context)