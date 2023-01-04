from django.db import models

# Create your models here.

class Todo(models.Model):
    topic = models.CharField(max_length=100,unique=True)
    describe = models.CharField(max_length = 100 )
    time_remaning = models.CharField(max_length=10)