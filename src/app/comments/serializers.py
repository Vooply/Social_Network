from app.comments.models import Comment
from rest_framework import serializers
from app.likes import services as likes_services


class CommentSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'body',
            'created_at',
            'total_likes',
            'is_fan',
        )

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "body")
