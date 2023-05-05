from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsAccountOwner
from .models import Follower
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404
from books.models import Book
from utils.permissions import IsAccountOwnerOrAdminOnlyGetOrAccountOwner


class FollowerView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        get_object_or_404(Book, id=book_id) 
        return serializer.save(user_id=self.request.user.id, book_id=book_id)


class FollowerDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdminOnlyGetOrAccountOwner]

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    lookup_field = "id"
