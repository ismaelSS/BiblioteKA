from apscheduler.schedulers.background import BackgroundScheduler
from .models import Schedules
from datetime import datetime
from django.utils import timezone
from.functions import block_user,unblock_user,check_retuned

def execute_function(function_name: str, schedule:Schedules):
    if function_name == "block user":
        block_user(schedule.loan)
    if function_name == "unblock user":
        unblock_user(schedule.loan)
    if function_name == "check returned":
        check_retuned(schedule.loan)



def my_task():
    current_time = timezone.now()
    schedules = Schedules.objects.filter(execution_date__lt=current_time)
    for schedule in schedules:
        ...


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_task, 'interval', seconds=5)
    scheduler.start()