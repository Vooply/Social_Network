from django.conf.urls import url
from django.urls import path

from app.users.views import CreateUserAPIView, AuthenticateUserAPIView, UserRetrieveUpdateAPIView

app_name = 'users'

urlpatterns = [
    path('register/', CreateUserAPIView.as_view()),
    path('auth/', AuthenticateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view())
]
