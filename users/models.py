from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("editor", "Editor"),
        ("reader", "Reader"),
    )
    PLAN_CHOICES = (
        ("info", "JOTA Info"),
        ("pro", "JOTA PRO"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="reader")
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default="info")

    def __str__(self):
        return f"{self.username} ({self.role})"
