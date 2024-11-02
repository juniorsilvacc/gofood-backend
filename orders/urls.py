from django.urls import path
from . import views


urlpatterns = [
    path('coupons/', views.CouponListCreateView.as_view(), name='coupon-create-list'),
    path('coupons/<int:pk>/', views.CouponRetrieveUpdateDestroy.as_view(), name='coupon-detail-update-destroy'),

    path('addresses/', views.AddressListCreateView.as_view(), name='address-create-list'),
    path('addresses/<int:pk>/', views.AddressRetrieveUpdateDestroy.as_view(), name='address-detail-update-destroy'),

    path('orders/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order-detail'),

    path('orderitems/', views.OrderItemCreateView.as_view(), name='orderitem-create'),
]
