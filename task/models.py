from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
