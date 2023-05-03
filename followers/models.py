from django.db import models
# from users.models import User
# from books.models import Book

# Create your models here.


class Follower(models.Model):
    class Meta:
        ordering = ("id",)

    user = models.ForeignKey("users.User", models.CASCADE)
    book = models.ForeignKey("books.Book", models.CASCADE)
