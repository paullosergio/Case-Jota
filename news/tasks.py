from celery import shared_task
from django.utils import timezone

from .models import News


@shared_task
def publish_scheduled_news():
    now = timezone.now()
    scheduled = News.objects.filter(status="draft", publish_at__lte=now)

    count = scheduled.update(status="published")
    return f"{count} notícias publicadas automaticamente."
