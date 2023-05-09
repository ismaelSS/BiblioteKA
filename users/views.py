from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from utils.permissions import (
    IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin,
    IsAdminOnlyGET,
)
from rest_framework import generics
import ipdb
from loans.models import Loan
from validation_erros.erros import ErrorForbidden


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOnlyGET]

    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerAndPathOrAcconuntOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"

    def perform_destroy(self, instance):
        loans = Loan.objects.filter(returned_at=None, user=instance)
        if not loans:
            return instance.delete()
        else:
            response = {"message": "Solve your issues"}
            raise ErrorForbidden(response)
