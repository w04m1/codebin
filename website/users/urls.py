from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, LoginAPIView, RegistrationAPIView


urlpatterns = [
    path("users/auth/login/", LoginAPIView.as_view(), name="login"),
    path(
        "users/auth/register/", RegistrationAPIView.as_view(), name="register"
    ),
    path(
        "users/auth/token/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "users/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
