from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from copies.views import CopyView
from copies.views import CopyDetailView

urlpatterns = [
    path("books/", views.BoookViews.as_view()),
    path("books/<int:pk>/", views.BoookDetailViews.as_view()),
    path("books/<int:pk>/copies/", CopyView.as_view()),
    path("books/copies/<int:pk>/", CopyDetailView.as_view()),
]
