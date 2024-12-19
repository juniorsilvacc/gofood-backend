from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-create-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='category-detail-update-destroy')
]
