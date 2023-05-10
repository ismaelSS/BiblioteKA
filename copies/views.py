from .models import Copy
from .serializers import CopySerializer
from rest_framework import generics
from utils.permissions import IsAdminDELETE
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from books.models import Book
from drf_spectacular.utils import extend_schema


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminDELETE]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk")
        get_object_or_404(Book, id=book_id)
        return serializer.save(book_id=book_id)

    @extend_schema(
        operation_id="Copy",
        summary="Busca um  copia",
        description="Busca uma cópia no banco de dados, com o ID da cópia passado como parâmetro. Esta rota requer autenticação, mas está disponível para todos os usuários.",
        responses={200: CopySerializer},
        tags=["Rotas de copies"],
    )
    def get(self, request, *args, **kwargs):
        self.queryset = Copy.objects.filter(book_id=kwargs.get("pk"))
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Copy",
        summary="Cria uma nova  copia",
        description="Cria uma copia de um livro, com o ID do livro passado como parâmetro. Está rota está limitada, somente adiministradores tem accesso.",
        responses={200: CopySerializer},
        tags=["Rotas de copies"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CopyDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminDELETE]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    @extend_schema(
        operation_id="Copy",
        summary="Deleta uma  copia",
        description="Deleta uma copia, com o ID passado como parâmetro. Está rota está limitada, somente adiministradores tem accesso.",
        responses={204: {}},
        tags=["Rotas de copies"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
