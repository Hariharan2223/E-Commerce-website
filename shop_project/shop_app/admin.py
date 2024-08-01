from django.contrib import admin
from .models import *

class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'created_at')

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class products_hariAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'vendor', 'quantity', 'original_price', 'selling_price', 'status', 'trending', 'created_at')

admin.site.register(category_hari, categoryAdmin)
admin.site.register(products_hari, products_hariAdmin)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
