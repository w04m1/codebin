from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Snippet  # Comment,; Reaction
from .serializers import (
    SnippetSerializer,
)  # CommentSerializer,; ReactionSerializer,


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Snippet.objects.filter(owner=self.request.user)
        return Snippet.objects.filter(public=True)

    def update(self, request, *args, **kwargs):
        snippet = self.get_object()
        if snippet.owner != request.user:
            return Response(
                {
                    "detail": "You do not have permission to perform this action."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
