from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsAdminOrOnlyGET
from drf_spectacular.utils import extend_schema


class BoookViews(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOnlyGET]

    get_serializer = BookSerializer
    queryset = Book.objects.all()

    pagination_class = PageNumberPagination

    @extend_schema(
        operation_id="Book",
        summary="Lista todos livros",
        description="Lista todos livros do banco de dados. Está rota é livre",
        responses={200: BookSerializer},
        tags=["Rotas de books"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Book",
        summary="Cria um novo livro",
        description="Cria um novo livro. Está rota está limitada, somente adiministradores tem accesso",
        responses={201: BookSerializer},
        tags=["Rotas de books"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class BoookDetailViews(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOnlyGET]

    queryset = Book.objects.all()
    get_serializer = BookSerializer

    allowed_methods = ["get", "delete", "patch"]

    @extend_schema(
        operation_id="Book",
        summary="Busca livros",
        description="Busca o livro no banco de dados, com o ID do livro passado como parâmetro. Está rota é livre.",
        responses={200: BookSerializer},
        tags=["Rotas de books"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Book",
        summary="Deleta livro",
        description="Deleta livro no banco de dados, com o ID do livro passado como parâmetro. Está rota está limitada, somente adiministradores tem accesso",
        responses={204: {}},
        tags=["Rotas de books"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        operation_id="Book",
        summary="Edita livro",
        description="Edita livro com o ID do livro passado como parâmetro. Está rota está limitada, somente adiministradores tem accesso",
        responses={200: BookSerializer},
        tags=["Rotas de books"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="Book",
        summary="Edita livro",
        description="Edita livro com o ID do livro passado como parâmetro. Está rota está limitada, somente adiministradores tem accesso",
        responses={200: BookSerializer},
        tags=["Rotas de books"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
