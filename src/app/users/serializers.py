from rest_framework import serializers

from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'date_joined', 'password')
        extra_fields = {'password': {'write_only': True}}

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value
    #
    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError({"username": "This username is already in use."})
    #     return value
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data['email']
    #     instance.username = validated_data['username']
    #     instance.password = validated_data['password']
    #
    #     instance.save()
    #
    #     return instance