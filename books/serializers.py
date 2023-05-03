from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "afferword",
            "publisher",
            "publication_date",
            "language",
        ]

        extra_kwargs = {
            "pages": {"required": False},
            "afferword":  {"required": False},
            "publisher": {"required": False},
            "publication_date": {"required": False}
        }