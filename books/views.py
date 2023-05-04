from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

import ipdb


class BoookViews(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    get_serializer = BookSerializer
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination


class BoookDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    get_serializer = BookSerializer
    ...
