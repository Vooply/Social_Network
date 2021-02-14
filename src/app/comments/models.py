from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from app.common.models import BaseDateAuditModel
from app.likes.models import Like
from config import settings


class Comment(BaseDateAuditModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comemnts', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    body = models.TextField
    likes = GenericRelation(Like)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()

    class Mets:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        Index(fields=("post",))
