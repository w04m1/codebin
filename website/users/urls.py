from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, RegistrationAPIView, UserAPIView


urlpatterns = [
    path("auth/sign-up/", RegistrationAPIView.as_view(), name="sign_up"),
    re_path(
        r"^auth/(token|login)/$",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("user/", UserAPIView.as_view(), name="user"),
]
