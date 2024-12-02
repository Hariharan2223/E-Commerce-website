import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

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

    
