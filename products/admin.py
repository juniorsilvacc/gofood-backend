from django.contrib import admin
from products.models import Product, Option, Additional
from django.utils.html import format_html


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
    list_display = ('id', 'display_image', 'name', 'category', 'price', 'active',)
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('price', 'active',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 35px; height: auto;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'
