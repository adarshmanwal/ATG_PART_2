from datetime import datetime
from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Group_Message(models.Model):
    user = models.CharField(max_length=10000)
    group_id=models.IntegerField()
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)