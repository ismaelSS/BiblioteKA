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
            "name",
            "is_admin",
            "created_at",
            "updated_at",
            "is_blocked"
        ]
        extra_kwargs = {"password": {"write_only": True}}

        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                if key == "password":
                    instance.set_password(value)
                else:
                    setattr(instance, key, value)