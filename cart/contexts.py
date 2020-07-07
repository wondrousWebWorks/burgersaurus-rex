from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Product

def cart_content(request):

    cart_items = []
    sub_total = 0
    order_total = 0
    product_count = 0
    delivery_threshold = settings.DELIVERY_THRESHOLD
    delivery_charge = settings.DELIVERY_CHARGE
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    order_total = delivery_charge + sub_total
    
    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'product_count': product_count,
        'delivery_threshold': delivery_threshold,
        'delivery_charge': delivery_charge,
        'order_total': order_total,
    }

    return context