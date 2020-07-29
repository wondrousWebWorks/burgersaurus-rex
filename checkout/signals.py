from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the order total on orderitem create/update
    """
    instance.order.update_order_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the order total on deletion of orderitem
    """
    instance.order.update_order_total()
