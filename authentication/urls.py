from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import RegisterUserView


urlpatterns = [
    path('authentication/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/verify', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', RegisterUserView.as_view(), name='register'),
]
