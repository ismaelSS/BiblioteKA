from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "user",
            "books",
        ]

