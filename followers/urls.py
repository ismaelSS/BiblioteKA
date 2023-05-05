from django.urls import path
from .import views


urlpatterns = [
    path("followers/", views.FollowerView.as_view()),
    path("followers/book/<int:book_id>/", views.FollowerView.as_view()),
    path("followers/<int:id>/", views.FollowerDetailView.as_view())
]
