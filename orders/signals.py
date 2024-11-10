from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def associate_order_item_to_order(sender, instance, created, **kwargs):
    pass
