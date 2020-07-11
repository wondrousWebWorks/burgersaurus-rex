from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect(reverse('menu'))
        
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqPsYKP14WGiq4LBCGkpzDps5JORfc9euGYZUeYnUBmby6Uzqcg0KMqQTuNDFw1dOOXHG3h4XH0QBoAeACTd46V00lnRRF4t9',
        'client_secret': 'test-client-secret',
    }

    return render(request, template, context)