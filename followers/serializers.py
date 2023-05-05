from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(read_only=True)
    book = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Follower.objects.create(**validated_data)

    class Meta:
        model = Follower
        fields = [
            "id",
            "user",
            "book",
        ]

