from loans.models import Loan
from .models import Schedules, FunctionsOptions
from django.utils import timezone
import dotenv
import os

dotenv.load_dotenv()


def block_user(loan: Loan):
    user = loan.user
    user.is_blocked = True
    user.save()


def unblock_user(loan: Loan):
    user = loan.user
    user.is_blocked = False
    user.save()


def schedule_unblock(loan: Loan):
    schedule_time = timezone.now() + timezone.timedelta(
        days=int(os.getenv("UNBLOCK_PERIOD"))
    )

    Schedules.objects.create(
        execution_date=schedule_time, function=FunctionsOptions.UNBLOCK_USER, loan=loan
    )


def check_retuned(loan: Loan):
    if not loan.returned_at:
        user = loan.user
        user.is_blocked = True
        user.save()


def devolution_event(loan: Loan):
    user = loan.user

    is_blocked = user.is_blocked
    user_loans_pending = user.loans.filter(returned_at__isnull=True)
    have_another_pending = user_loans_pending.count() >= 1

    copy = loan.copy
    copy.is_avaliable = True
    copy.save()

    is_in_time = timezone.now() < loan.return_date

    if is_in_time:
        if is_blocked:
            if have_another_pending:
                ...
            else:
                schedule_unblock(loan)
        else:
            ...
    elif have_another_pending:
        if is_blocked:
            ...
        else:
            block_user(loan)
    else:
        if is_blocked:
            schedule_unblock(loan)
        else:
            block_user(loan)
            schedule_unblock(loan)
