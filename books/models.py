from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ("id",)

    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    pages = models.IntegerField(null=True, blank=True)
    afterword = models.TextField(null=True, blank=True)
    publisher = models.TextField(max_length=100, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    language = models.TextField(max_length=30)
