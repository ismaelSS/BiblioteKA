from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Follower
from users.serializers import UserSerializer
from books.serializers import BookSerializer


class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    book = BookSerializer(required=False)

    class Meta:
        model = Follower
        fields = [
            "id",
            "user",
            "book",
        ]
