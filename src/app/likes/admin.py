from django.contrib import admin

from app.likes.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
