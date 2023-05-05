from users.models import User
from loans.models import Loan

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

# def check_retuned():

#     user_loans = user.loans