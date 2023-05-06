from users.models import User
from loans.models import Loan
from .models import Schedules, FunctionsOptions
from datetime import datetime, timedelta

def block_user(loan_id:int):
    loan = Loan.objects.get(id=loan_id)
    user = loan.user
    user.is_blocked = True
    user.save()

def unblock_user(loan_id:int):
    loan = Loan.objects.get(id=loan_id)
    user = loan.user
    user.is_blocked = False
    user.save()

def unblock_user_for_id(user_id: int):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        user = None

    if user != None:
        user.is_blocked = False
        user.save()


def schedule_unblock(user_id:int):
    schedule_time = datetime.now() + timedelta(days=2)

    Schedules.objects.create(
        execution_date=schedule_time,
        function=FunctionsOptions.UNBLOCK_USER,
        user_id=user_id
    )


# checagem feita na data maxima de devolução do livro
def check_retuned(loan_id: int):
    loan = Loan.objects.get(id=loan_id)

    if not loan.returned_at:
        user = loan.user
        user.is_blocked = True
        user.save()

def devolution_event(loan_id: int):
    loan = Loan.objects.get(id=loan_id)
    user = loan.user
    user_id = user_id

    is_blocked = user.is_blocked
    user_loans_pending = user.loans.filter(returned_at__isnull=True)
    have_another_pending = user_loans_pending.count() >= 2


    # redisponibilizando a copia
    copy = loan.copy
    copy.is_avaliable = True
    copy.save()

    is_in_time = datetime.now() < loan.return_date

    if is_in_time:
        if is_blocked:
            if have_another_pending:
                ...
            else:
                schedule_unblock(user_id)
        else:
            ...
    else:
        if have_another_pending:
            if is_blocked:
                ...
            else:
                block_user(loan_id)
        else:
            if is_blocked:
                schedule_unblock(user_id)
            else:
              block_user(loan.id)
              schedule_unblock(user_id)







