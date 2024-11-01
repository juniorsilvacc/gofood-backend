from rest_framework import generics
from products.models import Option
from products.models import Additional
from products.models import Product
from products.serializers import ProductSerializer, ProductListDetailSerializer, OptionSerializer, AdditionalSerializer, AdditionalListDetailSerializer


class OptionListCreateView(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AdditionalListCreateView(generics.ListCreateAPIView):
    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdditionalListDetailSerializer
        return AdditionalSerializer


class AdditionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Additional.objects.all()
    serializer_class = AdditionalSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdditionalListDetailSerializer
        return AdditionalSerializer


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


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListDetailSerializer
        return ProductSerializer
