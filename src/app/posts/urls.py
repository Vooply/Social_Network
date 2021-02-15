from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.posts.views import PostViewSet

app_name = 'posts'

router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    # path('comments/', include('app.comments.urls', namespace='comments')),
] + router.urls
