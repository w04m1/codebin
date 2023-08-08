from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, LoginAPIView, RegistrationAPIView


urlpatterns = [
    path("auth/login/", LoginAPIView.as_view(), name="login"),
    path("auth/register/", RegistrationAPIView.as_view(), name="register"),
    path(
        "auth/token/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
