from django import template

register = template.Library()


@register.filter(name='calculate_item_subtotal')
def calculate_item_subtotal(price, quantity):
    return price * quantity
