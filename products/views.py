from rest_framework import generics
from products.models import Option
from products.models import Product
from products.serializers import ProductSerializer, ProductListDetailSerializer, OptionSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Option"])
class OptionListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


@extend_schema(tags=["Option"])
class OptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


@extend_schema(tags=["Product"])
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

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []


@extend_schema(tags=["Product"])
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListDetailSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]
