from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('products.urls')),
    # path('api/v1/', include('options.urls')),
    # path('api/v1/', include('additionals.urls')),
    # path('api/v1/', include('coupons.urls')),
    # path('api/v1/', include('addresses.urls')),
    # path('api/v1/', include('orders.urls')),
    # path('api/v1/', include('items.urls')),
]
