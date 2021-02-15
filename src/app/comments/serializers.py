from rest_framework import serializers
from app.likes import services as likes_services
from app.comments.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['id', 'body', 'user', 'post', 'created', 'is_fan', 'total_likes']

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
