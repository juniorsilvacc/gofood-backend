from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-create-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='category-detail-update-destroy'),

    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
