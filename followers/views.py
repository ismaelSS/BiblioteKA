from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Follower
from books.models import Book
from .serializers import FollowerSerializer
from django.shortcuts import get_object_or_404
from utils.permissions import IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from books.models import Book
from validation_erros.erros import ErrorNotFound, ErrorForbidden
import ipdb


class FollowerView(generics.ListCreateAPIView, generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk")
        book = get_object_or_404(Book, id=book_id)
        return serializer.save(book=book, user_id=self.request.user.id)

    @extend_schema(
        operation_id="Follower",
        summary="Segue um livro",
        description="Segue um livro. Esta rota requer autenticação, mas está disponível para todos os usuários.",
        responses={200: FollowerSerializer},
        tags=["Rotas de followers"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="Follower",
        summary="Lista todos seguidores de um livro",
        description="Lista todos os seguidores de um livro. Está rota é livre",
        responses={200: FollowerSerializer},
        tags=["Rotas de followers"],
    )
    def get(self, request, *args, **kwargs):
        self.queryset = Follower.objects.filter(book_id=kwargs.get("pk"))
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Follower",
        summary="Deixa de seguir um livro",
        description="Deixa de seguir um livro. Esta rota requer autenticação, Somente o proprietário da conta pode para de seguir um livro.",
        responses={200: FollowerSerializer},
        tags=["Rotas de followers"],
    )
    def delete(self, request, *args, **kwargs):
        book = Book.objects.filter(id=kwargs.get("pk")).first()

        if not book:
            response = {"message": "Book not found!"}
            raise ErrorNotFound(response)

        follower = Follower.objects.filter(
            user_id=request.user.id,
            book_id=book.id,
        )

        if not follower:
            response = {"detail": "You do not have permission to perform this action."}
            raise ErrorForbidden(response, code=403)

        follower.delete()

        return Response(status=204)
