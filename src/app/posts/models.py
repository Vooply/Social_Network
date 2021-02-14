from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _

from app.common.models import BaseDateAuditModel
from app.likes.models import Like


class Post(BaseDateAuditModel):
    body = models.TextField
    title = models.CharField(max_length=50)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def title(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

        # indexes = [
        #     Index(fields=('title', ))
        # ]