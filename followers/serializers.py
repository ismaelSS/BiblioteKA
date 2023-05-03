from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = [
            "id",
            "user",
            "books",
        ]

