from django.apps import AppConfig
from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
