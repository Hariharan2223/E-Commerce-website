from django.contrib import admin
from .models import *
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description','created_at')


admin.site.register(Category_Hari,categoryAdmin)
admin.site.register(Products_Hari)