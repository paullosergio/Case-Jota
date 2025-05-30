from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "check-pending-news-every-minute": {
        "task": "news.tasks.publish_scheduled_news",
        "schedule": crontab(minute="*/1"),
    },
}
