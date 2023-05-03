from django.db import models


class Copie(models.Model):
    is_avaliable = models.BooleanField(default=True)
