from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# TODO: Have a thought about current state as Charfield for each task i.e either in "Started", "In Progress" or "Almost Done"

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Status(models.Model):
    is_finished = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now())
    finished_at = models.DateTimeField(null=True)

