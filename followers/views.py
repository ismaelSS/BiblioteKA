from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Follower
from books.models import Book
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin
from rest_framework.exceptions import PermissionDenied


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

    def delete(self, request, *args, **kwargs):
        follower = self.get_object()
        if follower.user != request.user:
            raise PermissionDenied("You are not allowed to unfollow this book.")
        return self.destroy(request, *args, **kwargs)
