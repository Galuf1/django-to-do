from email import charset
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()