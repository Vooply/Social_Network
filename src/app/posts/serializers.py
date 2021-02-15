from rest_framework import serializers

from app.likes import services as likes_services
from app.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

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
            'comments',
        )

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
