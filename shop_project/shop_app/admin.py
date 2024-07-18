from django.contrib import admin
from .models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description','created_at')


admin.site.register(category_hari,categoryAdmin)
admin.site.register(products_hari)