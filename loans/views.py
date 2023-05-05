from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import IsAdminUser, IsAdminOrOnlyGET
from loans.serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from copies.models import Copy
from loans.models import Loan


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrOnlyGET]
    serializer_class = LoanSerializer

    def perform_create(self, serializer) -> None:
        user = get_object_or_404(User, id=self.request.data.get("user_id"))
        copy = get_object_or_404(Copy, id=self.request.data.get("copy_id"))

        serializer.save(user=user, copy=copy)

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
