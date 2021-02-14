from django.contrib import admin

from app.comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass
