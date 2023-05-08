from django.urls import path
from .views import LoanView, LoanDetailView

urlpatterns = [
    path("loans/", LoanView.as_view()),
    path("loans/<int:pk>/", LoanDetailView.as_view()),
]
