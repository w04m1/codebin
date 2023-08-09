from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SnippetViewSet

router = DefaultRouter()
router.register("", SnippetViewSet)

urlpatterns = router.urls
