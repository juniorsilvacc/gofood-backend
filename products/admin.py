from django.contrib import admin
from products.models import Product, Option, Additional


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'addition', 'active',)
    search_fields = ('name',)


@admin.register(Additional)
class AdditionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'active',)
    search_fields = ('name',)
    list_filter = ('category',)
