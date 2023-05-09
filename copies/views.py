from .models import Copy
from .serializers import CopySerializer
from rest_framework import generics
from utils.permissions import IsAdminDELETE
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from books.models import Book


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminDELETE]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk")
        get_object_or_404(Book, id=book_id)
        return serializer.save(book_id=book_id)

    def get(self, request, *args, **kwargs):
        self.queryset = Copy.objects.filter(book_id=kwargs.get("pk"))
        return super().get(request, *args, **kwargs)


class CopyDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminDELETE]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer
