from rest_framework.routers import DefaultRouter

from app.comments.views import CommentsView

app_name = 'comments'
router = DefaultRouter()
router.register(r'', CommentsView)
urlpatterns = [
] + router.urls
