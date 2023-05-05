from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsAdminUser
import ipdb


class BoookViews(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]

    get_serializer = BookSerializer
    queryset = Book.objects.all()

    pagination_class = PageNumberPagination

    def permison_method(self):
        if self.request.method == "POST":
            permission_classes = [IsAdminUser]


class BoookDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Book.objects.all()
    get_serializer = BookSerializer

    def permison_method(self):
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]

    ...
