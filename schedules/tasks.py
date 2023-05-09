from apscheduler.schedulers.background import BackgroundScheduler
from .models import Schedules
from django.utils import timezone
from.functions import unblock_user,check_retuned
import dotenv
import os

dotenv.load_dotenv()


def execute_function(schedule:Schedules):
    if schedule.function == "unblock user":
        unblock_user(schedule.loan)
    if schedule.function == "check returned":
        check_retuned(schedule.loan)



def my_task():
    print('\033[32m' + 'script de schedules esta rodando!' + '\033[0m')
    current_time = timezone.now()
    schedules = Schedules.objects.filter(execution_date__lt=current_time)
    if not schedules:
        return
    for schedule in schedules:
        execute_function(schedule)
        schedules.delete()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_task, 'cron', day_of_week=os.getenv('OPERATING-DAYS'), hour=os.getenv('BUSSINESS-HOURS'), minute=0)
    scheduler.start()