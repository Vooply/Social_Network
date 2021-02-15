from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from app.likes.models import Like
from config import settings


class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    like = GenericRelation(Like)

    class Meta:
        ordering = ['created']

    @property
    def total_likes(self):
        return self.like.count()
