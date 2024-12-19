from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from orders.models import Coupon, Address, Order, OrderItem
from orders.serializers import CouponSerializer, AddressSerializer, OrderSerializer, OrderItemSerializer, OrderDetailSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(tags=["Coupon"])
class CouponListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


@extend_schema(tags=["Coupon"])
class CouponRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


@extend_schema(tags=["Address"])
class AddressCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    

@extend_schema(tags=["Address"])
class AddressListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@extend_schema(
    tags=["Order"],
    operation_id="create_order",
    description="Criação de pedidos, listagem de pedidos do usuário e consulta detalhada de pedidos.",
    request=OrderSerializer,
    examples=[
        OpenApiExample(
            "Exemplo de criação de Order",
            value={
                "change_due": "2.00",
                "coupon": 1,
                "address": 1,
                "payment": "CASH"
            },
            request_only=True,
        ),
        OpenApiExample(
            "Resposta de sucesso",
            value={
                "id": 1,
                "change_due": "2.00",
                "coupon": 1,
                "address": 1,
                "payment": "CASH"
            },
            response_only=True,
        ),
    ],
)
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

            order_data = OrderSerializer(order).data

            return Response({
                "message": "Pedido feito! O seu pedido já está em preparo.",
                "order": order_data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["OrderItem"],
    operation_id="create_order_item",
    description="Crie um novo item de pedido especificando o produto, adicionais e a quantidade.",
    request=OrderItemSerializer,
    examples=[
        OpenApiExample(
            "Exemplo de criação de OrderItem",
            value={
                "product_id": 1,
                "quantity": 2,
                "additionals": [1, 2],
            },
            request_only=True,
        ),
        OpenApiExample(
            "Resposta de sucesso",
            value={
                "id": 1,
                "product": 1,
                "quantity": 1,
                "price": 15.0,
                "description": "Hambúrguer nordestino",
                "options": [
                    1,
                    2
                ]
            },
            response_only=True,
        ),
    ],
)
class OrderItemCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            # Criar o OrderItem sem vinculação com uma Order
            order_item = serializer.save(order=None)
            return Response(OrderItemSerializer(order_item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Order"])
class OrderDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, *args, **kwargs):
        order = get_object_or_404(Order, id=id)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["Order"])
class MyOrdersListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
