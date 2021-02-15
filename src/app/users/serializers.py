from rest_framework import serializers

from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'date_joined', 'password')
        extra_fields = {'password': {'write_only': True}}
