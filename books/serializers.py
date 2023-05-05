from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .erros import ConflictError
import ipdb


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "pages",
            "afterword",
            "publisher",
            "publication_date",
            "language",
            "edition",
        ]

        extra_kwargs = {
            "pages": {"required": False},
            "afterword": {"required": False},
            "publisher": {"required": False},
            "publication_date": {"required": False},
            "edition": {"required": False},
        }

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        self.chek_book(validated_data=instance.__dict__)

        instance.save()

        return instance

    def create(self, validated_data):
        self.chek_book(validated_data=validated_data)
        return super().create(validated_data)

    def chek_book(self, validated_data):
        get_book = Book.objects.filter(
            title__iexact=validated_data.get("title"),
            author__iexact=validated_data.get("author"),
            language__iexact=validated_data.get("language"),
            edition__iexact=validated_data.get("edition"),
            publisher__iexact=validated_data.get("publisher"),
        ).first()

        if get_book:
            response = {"message": "The book already exists"}
            raise ConflictError(response)
