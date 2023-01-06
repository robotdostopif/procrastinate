from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# TODO: Have a thought about current state as Charfield for each task i.e either in "Started", "In Progress" or "Almost Done"

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(default=timezone.now(), blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

