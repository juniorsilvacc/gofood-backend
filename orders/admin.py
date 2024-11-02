from django.contrib import admin
from .models import Coupon, Address, Order, OrderItem


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'uses', 'active')
    readonly_fields = ('uses',)
    list_filter = ('active',)
    list_editable = ('active', 'discount',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'street', 'number', 'district', 'reference',)
    search_fields = ('zip_code', 'street',)
    list_filter = ('district',)


class OrderItemInline(admin.TabularInline):
    readonly_fields = ('product', 'quantity', 'price', 'description', 'additionals',)
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

    list_display = ('id', 'user', 'total', 'date', 'display_address', 'payment', 'delivered',)
    search_fields = ('user',)
    readonly_fields = ('user', 'total', 'change_due', 'payment', 'address', 'date',)

    def display_address(self, obj):
        return f"{obj.address.zip_code}, {obj.address.street}, {obj.address.district}, {obj.address.number}, {obj.address.reference}"
    display_address.short_description = 'Address'
admin.site.register(Order, OrderAdmin)
