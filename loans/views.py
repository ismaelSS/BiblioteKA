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

dotenv.load_dotenv()


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOnlyGET]
    serializer_class = LoanSerializer

    def perform_create(self, serializer) -> None:
        user = get_object_or_404(User, id=self.request.data.get("user_id"))
        copy = get_object_or_404(Copy, id=self.request.data.get("copy_id"))

        scheduled_date = timezone.now() + timezone.timedelta(days=int(os.getenv("RETURN_PERIOD")))

        loan = serializer.save(user=user, copy=copy, return_date = scheduled_date)

        Schedules.objects.create(
            execution_date=scheduled_date,
            function=FunctionsOptions.CHECK_RETURNED,
            loan=loan
        )


    def get_queryset(self):
        if self.request.user.is_superuser:
            user_id = self.request.query_params.get("user", None)

            if user_id:
                return Loan.objects.filter(user_id=int(user_id))

            return Loan.objects.all()

        return Loan.objects.filter(user=self.request.user)

class LoanDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()

    def patch(self, request, *args, **kwargs):
        update = self.partial_update(request, *args, **kwargs)
        loan = self.get_object()
        print(loan)
        devolution_event(loan)
        return update

    def put(self, request, *args, **kwargs):
        update = self.update(request, *args, **kwargs)
        loan = self.get_object()
        devolution_event(loan)
        return update
