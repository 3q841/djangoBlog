from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

PRIORITY = [
    ("H", "High"),
    ("L", "Low"),
    ("M", "Medium")
]

class Question(models.Model):
    title                   = models.CharField(max_length=70)
    Question                = models.TextField(max_length=200)
    priority                = models.CharField(max_length=1,choices=PRIORITY)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "The Question"
        verbose_name_plural ="Peoples Question"