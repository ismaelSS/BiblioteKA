from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "username",
            "is_admin",
            "created_at",
            "updated_at",
            "is_blocked"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if 'is_admin' in validated_data and validated_data['is_admin'] == True :
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

