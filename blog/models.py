from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Blogl(models.Model):
    STATUS=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=200)
    body=models.TextField()
    athor=models.ForeignKey(User,on_delete=models.CASCADE(),related_name='blog_post')
    status=models.CharField(max_length=15,choices=STATUS,default='draft')
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('publish',)
    def __str__(self):
        return self.title