from django.urls import path
from .import views


urlpatterns = [
    path("followers/", views.FollowerView.as_view()),
    path("followers/book/<int:pk>/", views.FollowerView.as_view()),
    path("followers/<int:pk>/", views.FollowerDetailView.as_view())

]
