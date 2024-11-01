from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
