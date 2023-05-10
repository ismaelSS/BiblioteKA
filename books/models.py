from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    class Meta:
        ordering = ("id",)

    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    pages = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(50560)])
    afterword = models.TextField(null=True, blank=True)
    publisher = models.TextField(max_length=100, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    language = models.TextField(max_length=30)
    edition = models.CharField(max_length=100, null=True, blank=True)
