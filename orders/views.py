from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from orders.models import Coupon, Address, Order, OrderItem
from orders.serializers import CouponSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, OrderDetailSerializer
from rest_framework.permissions import IsAuthenticated


class CouponListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class AddressListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class OrderCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Criar a Order vinculada ao usuário
            order = serializer.save(user=request.user)

            # Vincular OrderItems que ainda não têm uma Order associada
            order_items = OrderItem.objects.filter(order__isnull=True)
            for item in order_items:
                item.order = order
                item.save()

            return Response({
                "message": "Pedido feito! O seu pedido já está em preparo."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            # Criar o OrderItem sem vinculação com uma Order
            order_item = serializer.save(order=None)
            return Response(OrderItemSerializer(order_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        order = get_object_or_404(Order, id=id)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
