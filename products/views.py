from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer, ProductListDetailSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListDetailSerializer
        return ProductSerializer
