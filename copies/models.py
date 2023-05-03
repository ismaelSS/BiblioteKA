from django.db import models


class Copie(models.Model):
    is_avaliable = models.BooleanField(default=True)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )
