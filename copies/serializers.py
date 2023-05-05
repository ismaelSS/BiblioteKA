from rest_framework import serializers
from .models import Copy
from books.serializers import BookSerializer


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(required=False)
    class Meta:
        model = Copy
        fields = [
            "id",
            "is_avaliable",
            "book"

        ]
