from django.shortcuts import render
from .models import Copy
from .serializers import CopySerializer
from rest_framework import generics
from utils.permissions import IsAccountOwnerOrAdminOnlyGetOrAccountOwner
from utils.permissions import IsAccountOwner, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class CopyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer
    lookup_field = "id"
