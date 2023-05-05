from django.shortcuts import render
from .models import Copy
from .serializers import CopySerializer
from rest_framework import generics
from utils.permissions import IsAccountOwnerOrAdminOnlyGetOrAccountOwner
from utils.permissions import IsAccountOwner, IsAdminUser, IsAdminDELETE
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from books.models import Book


class CopyView(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminDELETE]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk")
        get_object_or_404(Book, id=book_id)
        return serializer.save(book_id=book_id)
