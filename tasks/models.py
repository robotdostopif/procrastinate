from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# TODO: Have a thought about current state as Charfield for each task i.e either in "Started", "In Progress" or "Almost Done"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(default=timezone.now(), blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    app_user = models.ForeignKey("AppUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    app_user = models.ForeignKey(
        "AppUser", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
