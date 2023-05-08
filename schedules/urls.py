from django.urls import path
from .views import SchedulesView

urlpatterns = [
    path("schedules/", SchedulesView.as_view()),
]