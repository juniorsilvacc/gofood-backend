from django.urls import path
from . import views


urlpatterns = [
    path('options/', views.OptionListCreateView.as_view(), name='option-create-list'),
    path('options/<int:pk>/', views.OptionRetrieveUpdateDestroy.as_view(), name='option-detail-update-destroy'),

    path('products/', views.ProductListCreateView.as_view(), name='product-create-list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-detail-update-destroy'),
]
