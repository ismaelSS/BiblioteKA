from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    password_validators = [
        validators.RegexValidator(
            r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=\[\]{};:\'",.<>/?\\|~-]).{8,}$',
            'The password must contain at least one uppercase letter, one lowercase letter, one number, one special character, and be at least 8 characters long.'
        )
    ]

    password = serializers.CharField(write_only=True, validators=password_validators)

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

