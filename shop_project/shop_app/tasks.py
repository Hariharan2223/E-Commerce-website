from celery import shared_task
from django.core.mail import send_mail
from .models import OrderItem
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_order_confirmation_email(email, order_id):
    try:
        # Get all the items in the order
        order_items = OrderItem.objects.filter(order_id=order_id)
        
        # Create a message with the order details
        item_list = ""
        for item in order_items:
            item_list += f'{item.product.name} (Quantity: {item.quantity}) - ${item.price}\n'
        
        subject = 'Order Confirmation of ShopCart'
        message = (
            f'Thank you for your order!\n\n'
            f'Your Order ID is {order_id}.\n\n'
            f'Here are the details of your purchase:\n\n'
            f'{item_list}\n'
            f'Total: ${sum(item.price for item in order_items)}\n\n'
            f'We hope to serve you again soon!'
        )

        # Send email
        send_mail(subject, message, 'shopcart@gmail.com', [email], fail_silently=False)
        
        logger.info(f'Order confirmation email sent to {email} for Order ID {order_id}')
    
    except Exception as e:
        logger.error(f'Failed to send email to {email} for Order ID {order_id}: {e}')
        raise
