from django.urls import path, re_path
from .consumers import SearchSuggestionConsumer, ProductStockConsumer, SaleConsumer

websocket_urlpatterns = [
    path('ws/search/', SearchSuggestionConsumer.as_asgi()),
    path('ws/stock/<int:product_id>/', ProductStockConsumer.as_asgi()),
    path('ws/sale/', SaleConsumer.as_asgi()),

]
