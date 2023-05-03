from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ("id",)
        
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    pages = models.IntegerField()
    afferword = models.TextField()
    publisher = models.TextField(max_length=100)
    publication_date = models.DateField()
    language = models.TextField(max_length=30)