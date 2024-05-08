from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=150)
    content = models.TextField()
    views = models.IntegerField(default=0)
    
class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    views = models.IntegerField(default=0)