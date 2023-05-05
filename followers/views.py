from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Follower
from books.models import Book
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin


class FollowerView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk")
        book = get_object_or_404(Book, id=book_id)
        return serializer.save(book=book, user_id=self.request.user.id)


class FollowerDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
