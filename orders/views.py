from rest_framework import generics
from orders.models import Coupon, Address
from orders.serializers import CouponSerializer, AddressSerializer


class CouponListCreateView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
