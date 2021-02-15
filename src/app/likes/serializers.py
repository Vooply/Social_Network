from rest_framework import serializers

from app.likes.models import Like
from app.users.models import User


class FanSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username',)

    def get_username(self, obj):
        return obj.get_username()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "object_id",
            "user",
            "content_type",
        )
