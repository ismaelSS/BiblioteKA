from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer, LoginSerializer
from utils.permissions import (
    IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin,
    IsAdminOnlyGET,
)
from rest_framework import generics
from loans.models import Loan
from validation_erros.erros import ErrorForbidden
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOnlyGET]

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="User",
        summary="Lista todos usuários",
        description="Lista todos usuários do banco de dados. Essa rota é apenas para administradores.",
        responses={200: UserSerializer},
        tags=[
            "Rotas de usuários",
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="User",
        summary="Cria um novo usuários",
        description="Cria um novo usuário. Esta rota é livre e não requer autenticação.",
        responses={200: UserSerializer},
        tags=["Rotas de usuários"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    allowed_methods = ["get", "delete", "patch"]

    def perform_destroy(self, instance):
        loans = Loan.objects.filter(returned_at=None, user=instance)
        if not loans:
            return instance.delete()
        else:
            response = {"message": "Solve your issues"}
            raise ErrorForbidden(response)

    @extend_schema(
        operation_id="User",
        summary="Busca um usuários",
        description="Busca um usuário no banco de dados. Esta rota requer autenticação e o ID do usuário deve ser passado como parâmetro. Só é possível fazer a busca do próprio usuário ou se o usuário for um administrador.",
        responses={200: UserSerializer},
        tags=["Rotas de usuários"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="User",
        summary="Exclui um  usuários",
        description="Exclui um usuário do banco de dados. Esta rota requer autenticação e o ID do usuário deve ser passado como parâmetro. Só é possível excluir o próprio usuário ou se o usuário for um administrador.",
        responses={204: {}},
        tags=["Rotas de usuários"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(
        operation_id="User",
        summary="Edita um  usuários",
        description="Edita um usuários do banco de dados. Esta rota requer autenticação e o ID do usuário deve ser passado como parâmetro. Só é possível editar o próprio usuário ou se o usuário for um administrador.",
        responses={200: UserSerializer},
        tags=["Rotas de usuários"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="User",
        summary="Edita um  usuários",
        description="Edita um usuários do banco de dados. Esta rota requer autenticação e o ID do usuário deve ser passado como parâmetro. Só é possível editar o próprio usuário ou se o usuário for um administrador.",
        responses={200: UserSerializer},
        tags=["Rotas de usuários"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class LoginView(TokenObtainPairView):
    @extend_schema(
        operation_id="User",
        summary="Faz login",
        description="Faz login na aplicação. Está rota é livre",
        responses={200: LoginSerializer},
        tags=["Rotas de login"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
