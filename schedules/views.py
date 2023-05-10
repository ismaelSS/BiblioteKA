from django.shortcuts import render
from .serializers import SchedulesSerializer
from .models import Schedules
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema


class SchedulesView(ListCreateAPIView):
    serializer_class = SchedulesSerializer
    queryset = Schedules.objects.all()

    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
