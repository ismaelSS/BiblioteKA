from django.urls import path
from . import views


urlpatterns = [
    path("followers/book/<int:pk>/", views.FollowerView.as_view()),
]
