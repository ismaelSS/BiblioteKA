from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("books/", views.BoookViews.as_view()),
    path("books/<int:pk>/", views.BoookDetailViews.as_view()),
]
