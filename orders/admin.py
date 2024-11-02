from django.contrib import admin
from .models import Coupon, Address, Order, OrderItem


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'uses', 'active')
    search_fields = ('code',)
    readonly_fields = ('uses',)
    list_filter = ('active',)
    list_editable = ('active', 'discount',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'street', 'number', 'district', 'reference',)
    search_fields = ('zip_code', 'street',)
    list_filter = ('district',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'date', 'display_address', 'payment', 'delivered',)
    search_fields = ('user',)
    readonly_fields = ('user', 'total', 'date', 'change_due', 'payment', 'address',)

    def display_address(self, obj):
        return f"{obj.address.zip_code}, {obj.address.street}, {obj.address.district}, {obj.address.number}, {obj.address.reference}"
    display_address.short_description = 'Address'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'created_at', 'updated_at',)
    list_filter = ('order', 'product')
    search_fields = ('product__name', 'order__id')
    readonly_fields = ('created_at', 'updated_at')
