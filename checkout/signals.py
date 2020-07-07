from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_order_total()