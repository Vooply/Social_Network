from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from app.comments.models import Comments
from app.comments.serializers import CommentsSerializer
from app.common.permissions import IsOwnerOrReadOnly
from app.likes.mixin import LikedMixin


class CommentsView(LikedMixin, ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
