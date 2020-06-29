from django.conf import settings
from decimal import Decimal

def cart_content(request):

    cart_items = []
    order_total = 0
    product_count = 0
    delivery_threshold = settings.DELIVERY_THRESHOLD
    delivery_charge = settings.DELIVERY_CHARGE

    grand_total = delivery_charge + order_total
    
    context = {
        'cart_items': cart_items,
        'order_total': order_total,
        'product_count': product_count,
        'delivery_threshold': delivery_threshold,
        'delivery_charge': delivery_charge,
        'grand_total': grand_total,
    }

    return context