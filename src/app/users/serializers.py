from rest_framework import serializers

from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'posts', 'date_joined', 'password', 'comments')
        extra_fields = {'password': {'write_only': True}}
