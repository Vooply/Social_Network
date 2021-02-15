from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters import rest_framework as rfilters
from rest_framework.decorators import action

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet

from app.comments.models import Comment
from app.comments.serializers import CommentSerializer, CommentCreateSerializer
from app.likes.mixin import LikedMixin


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)



# class CommentListApiView(GenericViewSet, ListAPIView):
#     """
#         CommentList.
#         Users can see all post's comments
#     """
#
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     filter_backends = [filters.OrderingFilter, rfilters.DjangoFilterBackend]
#     filterset_fields = ("post",)
#     ordering_fields = ["post"]
#
#     def get_queryset(self):
#         return Comment.objects.filter(post_id=self.kwargs.get("post_pk", None))


# class CommentCreateApiView(CreateAPIView, ViewSet):
#     """
#         CommentCreateApiView.
#         Authorized users can also add new comments to posts
#     """
#
#     queryset = Comment.objects.all()
#     serializer_class = CommentCreateSerializer
#
#     @action(detail=False, methods=['POST'])
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user, post=self.kwargs.get("post_pk", None))


class CommentDetailApiView(LikedMixin, RetrieveUpdateDestroyAPIView):
    """
        CommentDetail.
        Authorized users can update or delete their comments
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "comment_pk"

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        request.data["owner"] = self.request.user.id
        response = super().update(request, *args, **kwargs)

        return response
