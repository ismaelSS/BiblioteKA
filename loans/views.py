from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsAdminUser, IsAdminOrOnlyGET
from loans.serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from copies.models import Copy
from loans.models import Loan
from schedules.models import Schedules, FunctionsOptions
from schedules.functions import devolution_event
from django.utils import timezone
import dotenv
import os
import ipdb
from drf_spectacular.utils import extend_schema

from validation_erros.erros import ConflictError, ErrorForbidden

dotenv.load_dotenv()


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOnlyGET]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def perform_create(self, serializer) -> None:
        user = get_object_or_404(User, id=self.request.data.get("user_id"))
        copy = get_object_or_404(Copy, id=self.request.data.get("copy_id"))

        loans = Loan.objects.filter(user=user, returned_at=None)

        if loans.count() >= 3:
            response = {"message": "The limit of loans is 3."}
            raise ErrorForbidden(response)

        if not copy.is_avaliable:
            response = {"message": "The copy is already in use."}
            raise ConflictError(response)

        scheduled_date = timezone.now() + timezone.timedelta(
            days=int(os.getenv("RETURN_PERIOD", "7"))
        )

        if scheduled_date.weekday() >= 5:
            days_until_monday = 7 - scheduled_date.weekday()
            scheduled_date = scheduled_date + datetime.timedelta(days=days_until_monday)

        loan = serializer.save(
            user=user,
            copy=copy,
            return_date=scheduled_date,
        )

        copy.is_avaliable = False
        copy.save()

        Schedules.objects.create(
            execution_date=scheduled_date,
            function=FunctionsOptions.CHECK_RETURNED,
            loan=loan,
        )

    def get_queryset(self):
        if self.request.user.is_superuser:
            user_id = self.request.query_params.get("user", None)

            if user_id:
                return Loan.objects.filter(user_id=int(user_id))

            return Loan.objects.all()

        return Loan.objects.filter(user=self.request.user)

    @extend_schema(
        operation_id="Loan",
        summary="Lista todos os emprestimos",
        description="Lista todos os emprestimos. Está rota está limitada, somente adiministradores tem accesso.",
        responses={200: LoanSerializer},
        tags=["Rotas de loans"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="Loan",
        summary="Cria um novo emprestimos",
        description="Cria um novo emprestimos. Está rota está limitada, somente adiministradores tem accesso.",
        responses={200: LoanSerializer},
        tags=["Rotas de loans"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoanDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    allowed_methods = ["patch"]

    @extend_schema(
        operation_id="Loan",
        summary="Devolução de um de um livro alocado",
        description="Faz  a devolução de um livro alcocado. Está rota está limitada, somente adiministradores tem accesso.",
        responses={200: LoanSerializer},
        tags=["Rotas de loans"],
    )
    def patch(self, request, *args, **kwargs):
        returned_at = request.data.get("returned_at", None)
        if returned_at is None:
            request.data["returned_at"] = timezone.now()
        update = self.partial_update(request, *args, **kwargs)
        loan = self.get_object()
        devolution_event(loan)
        return update
