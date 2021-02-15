from rest_framework import serializers

from app.likes import services as likes_services
from app.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'body',
            'created_at',
            'total_likes',
            'is_fan',
        )

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
