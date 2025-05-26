from django.db import models
from django.utils import timezone

from users.models import User


class News(models.Model):
    STATUS_CHOICES = (
        ("draft", "Rascunho"),
        ("published", "Publicado"),
    )

    VERTICAL_CHOICES = (
        ("poder", "Poder"),
        ("tributos", "Tributos"),
        ("saúde", "Saúde"),
        ("energia", "Energia"),
        ("trabalhista", "Trabalhista"),
    )
    name = models.CharField(max_length=50, choices=VERTICAL_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to="news_images/", null=True, blank=True)
    content = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    is_pro_only = models.BooleanField(default=False)
    vertical = models.CharField(max_length=50, choices=VERTICAL_CHOICES, default="poder")

    class Meta:
        ordering = ["-publish_at"]

    def __str__(self):
        return self.title

    def is_published(self):
        return self.status == "published" and self.publish_at <= timezone.now()
