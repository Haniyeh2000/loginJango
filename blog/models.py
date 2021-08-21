from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Blogl(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    #image
    #date
    #auter

    def __str__(self):
        return self.title