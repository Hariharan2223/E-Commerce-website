import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone 
from datetime import timedelta
from asgiref.sync import sync_to_async







class SaleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'sales_notifications'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        await self.send_sale_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_products(self):
        from .models import products_hari, ProductImage
        from django.utils.timezone import timedelta
        from django.conf import settings
        products = products_hari.objects.filter(trending=False)
        data = []

        for product in products:
            if product.sale_start_time:
                sale_end_time = product.sale_start_time + timedelta(minutes=1)
                time_left = (sale_end_time - timezone.localtime()).total_seconds()
                if time_left > 0:
                    first_image = ProductImage.objects.filter(product=product).first()
                    image_url = f"{settings.MEDIA_URL}{first_image.image}" if first_image else None
                    data.append({
                        'name': product.name,
                        'time_left': int(time_left),
                        'selling_price': product.selling_price,
                        'offer_price': product.selling_price * 75 / 100,
                        'category_name': product.category.name,
                        'images': image_url, 
                    })
        return data

    async def send_sale_data(self):
        data = await self.get_products()
        await self.send(text_data=json.dumps({'products': data}))

    async def notify_sale_update(self, event):
        data = [event['data']]
        await self.send(text_data=json.dumps(data))
        

class SearchSuggestionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
       
        pass

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            query = data.get('query', '').strip()

            if query:
                
                suggestions = await self.get_suggestions(query)
            else:
                suggestions = []


            await self.send(json.dumps({"suggestions": suggestions}))

        except Exception as e:
            await self.send(json.dumps({"error": str(e)}))

    @database_sync_to_async
    def get_suggestions(self, query):
        """
        Perform the database query in a thread-safe way.
        """
        from .models import products_hari
        products = products_hari.objects.filter(name__icontains=query)[:5]
        suggestions = [
            {"name": product.name, "image": product.images.first().image.url}
            for product in products
        ]
        return suggestions
    

class ProductStockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.room_group_name = f'product_{self.product_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def stock_update(self, event):
        await self.send(text_data=json.dumps({
            'stock': event['stock'],
        }))

