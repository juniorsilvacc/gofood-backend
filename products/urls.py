from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-create-list'),
    path('products/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='product-detail-update-destroy'),
]
