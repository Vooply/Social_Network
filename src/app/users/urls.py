from django.urls import path

from app.users.views import CreateUserAPIView, UserRetrieveUpdateAPIView, AuthenticateUserAPIView

app_name = 'users'

urlpatterns = [
    path('register/', CreateUserAPIView.as_view()),
    path('auth/', AuthenticateUserAPIView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]
