from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.common.models import BaseDateAuditModel
from app.likes.models import Like
from config import settings


class Post(BaseDateAuditModel):
    body = models.TextField()
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
