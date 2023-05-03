from django.db import models


class Loan(models.Model):
    allocated_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    retuned_at = models.DateTimeField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="loans"
    )

    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.PROTECT,
        related_name="book"
    )
