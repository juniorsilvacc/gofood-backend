from django.contrib import admin
from products.models import Product, Category, Additional

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'active',)
    search_fields = ('name',)
    list_filter = ('category',)
