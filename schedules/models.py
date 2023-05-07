from django.db import models

class FunctionsOptions(models.TextChoices):
    BLOCK_USER = "block user"
    UNBLOCK_USER = "unblock user"
    CHECK_RETURNED = "check returned"

class Schedules(models.Model):
    execution_date = models.DateTimeField()
    function = models.CharField(max_length=20, choices=FunctionsOptions.choices)
    user_id=models.IntegerField(null=True)

    loan = models.OneToOneField(
        "loans.Loan",
        on_delete=models.CASCADE,
        related_name="schedule",
        null=True
    )

def __repr__(self):
    return f'{self.function} | {self.execution_date}'


