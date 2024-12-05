
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import category_hari, products_hari, ProductImage
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils.timezone import timedelta, localtime
from django.conf import settings



@receiver(post_save, sender=category_hari)
@receiver(post_delete, sender=category_hari)
def clear_category_cache(sender, **kwargs):
    cache.delete('category_list')



# @receiver(post_save, sender=products_hari)
# def product_stock_update(sender, instance, **kwargs):


#     channel_layer = get_channel_layer()
#     group_name = f'product_{instance.id}'

#     async_to_sync(channel_layer.group_send)(
#         group_name,
#         {
#             'type': 'stock_update', 
#             'stock': instance.quantity, 
#         }
#     )


previous_state = {}

@receiver(pre_save, sender=products_hari)
def cache_previous_state(sender, instance, **kwargs):
    try:
        previous = sender.objects.get(pk=instance.pk)
        previous_state[instance.pk] = {
            'quantity': previous.quantity,
            'sale_start_time': previous.sale_start_time,
        }
    except sender.DoesNotExist:
        previous_state[instance.pk] = None 


@receiver(post_save, sender=products_hari)
def product_update_signal(sender, instance, **kwargs):
    previous = previous_state.get(instance.pk)
    channel_layer = get_channel_layer()

    if previous:
        if previous['quantity'] != instance.quantity:
            group_name = f'product_{instance.id}' 
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'stock_update',
                    'stock': instance.quantity,
                }
            )

        if previous['sale_start_time'] != instance.sale_start_time:
            sale_end_time = instance.sale_start_time + timedelta(minutes=1)
            time_left = (sale_end_time - localtime()).total_seconds()

            if time_left > 0:
                first_image = ProductImage.objects.filter(product=instance).first()
                image_url = f"{settings.MEDIA_URL}{first_image.image}" if first_image else None

                sales_data = {
                    'id': instance.id,
                    'name': instance.name,
                    'time_left': int(time_left),
                    'selling_price': instance.selling_price,
                    'offer_price': instance.selling_price * 75 / 100,
                    'category_name': instance.category.name,
                    'images': image_url,
                }

                async_to_sync(channel_layer.group_send)(
                    'sales_notifications', 
                    {
                        'type': 'notify_sale_update',
                        'data': sales_data,
                    }
                )
    else:
        print("New object created. No specific group messaging required.")


    previous_state.pop(instance.pk, None)

