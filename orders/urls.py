from django.urls import path
from . import views


urlpatterns = [
    path('coupons/', views.CouponListCreateView.as_view(), name='coupon-create-list'),
    path('coupons/<int:pk>/', views.CouponRetrieveUpdateDestroy.as_view(), name='coupon-detail-update-destroy'),

    path('addresses/', views.AddressListCreateView.as_view(), name='address-create-list'),
    path('addresses/<int:pk>/', views.AddressRetrieveUpdateDestroy.as_view(), name='address-detail-update-destroy'),
]
