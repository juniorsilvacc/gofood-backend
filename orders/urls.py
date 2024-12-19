from django.urls import path
from . import views


urlpatterns = [
    path('coupons/', views.CouponListCreateView.as_view(), name='coupon-create-list'),
    path('coupons/<int:pk>/', views.CouponRetrieveUpdateDestroy.as_view(), name='coupon-detail-update-destroy'),

    path('addresses/create/', views.AddressCreateView.as_view(), name='address-create'),
    path('addresses/list/', views.AddressListView.as_view(), name='addresses-list'),

    path('orders/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:id>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/my-orders/', views.MyOrdersListView.as_view(), name='my-orders'),

    path('orderitems/', views.OrderItemCreateView.as_view(), name='orderitem-create'),
]
