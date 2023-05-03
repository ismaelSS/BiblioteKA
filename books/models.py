from django.db import models


class Book(models.Model):
    title = models.TextField(max_length=100, min=3)
    author = models.TextField(max_length=100)
    pages = models.IntegerField()
    afferword = models.TextField()
    publisher = models.TextField(max_length=100)
    publication_date = models.DateField()
    language = models.TextField(max_length=30)