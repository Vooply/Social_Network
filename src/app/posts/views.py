from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.common.permissions import IsOwnerOrReadOnly
from app.likes.mixin import LikedMixin
from app.posts.models import Post
from app.posts.serializers import PostSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
