from typing import Tuple
from django.contrib import admin
from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('name', 'price', 'store')


class ClientAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = ('name', 'email', 'age')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
