
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import category_hari, products_hari
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=category_hari)
@receiver(post_delete, sender=category_hari)
def clear_category_cache(sender, **kwargs):
    cache.delete('category_list')



@receiver(post_save, sender=products_hari)
def product_stock_update(sender, instance, **kwargs):
    # Only send a notification if the quantity changes
    print("hi")
    # Check if the stock (quantity) has changed
    channel_layer = get_channel_layer()
    group_name = f'product_{instance.id}'
    print("hi2")
    # Ensure the group_send call is executed asynchronously using async_to_sync
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'stock_update',  # Type to trigger the method in consumer
            'stock': instance.quantity,  # Assuming `quantity` holds the stock
        }
    )
    print("hello")
