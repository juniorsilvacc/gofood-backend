# views.py
from rest_framework import generics
from authentication.serializers import RegisterUserSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["v1"])
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
