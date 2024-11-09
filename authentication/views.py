# views.py
from rest_framework import generics
from authentication.serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
