from django.contrib import admin
from .models import Coupon, Address


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'uses', 'active')
    search_fields = ('code',)
    readonly_fields = ('uses',)
    list_filter = ('active',)
    list_editable = ('active', 'discount',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('zip_code', 'street', 'number', 'district', 'reference')
    search_fields = ('zip_code', 'street')
    list_filter = ('district',)
