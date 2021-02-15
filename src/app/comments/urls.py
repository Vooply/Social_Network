from django.urls import path
from rest_framework.routers import DefaultRouter

from app.comments.views import CommentDetailApiView, CommentViewSet

app_name = 'comments'
router = DefaultRouter()
router.register('', CommentViewSet)

urlpatterns = [
    # path("", CommentListApiView.as_view({'get': "list"}), name="comments_list"),
    # path('', CommentCreateApiView.as_view({'post': "create"}), name='comment_create'),
    # path("comments/<int:comment_pk>/", CommentDetailApiView.as_view(), name="comment_detail", ),
] + router.urls
