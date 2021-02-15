from django.urls import path, include

app_name = 'likes'


urlpatterns = [
    path('', include('app.posts.urls', namespace='posts'))
]
