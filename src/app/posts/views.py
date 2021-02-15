from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.likes.mixin import LikedMixin
from app.posts.models import Post
from app.posts.serializers import PostSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
