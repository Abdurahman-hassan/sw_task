from celery import Celery

# from celery.schedules import crontab
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings.development')

app = Celery("app_config")
app.conf.update(**settings.CELERY_CONFIG)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.beat_schedule = {}
