from django.shortcuts import render
from .serializers import SchedulesSerializer
from .models import Schedules
from rest_framework.generics import ListCreateAPIView

class SchedulesView(ListCreateAPIView):
    serializer_class = SchedulesSerializer
    queryset = Schedules.objects.all()

