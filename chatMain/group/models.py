from datetime import datetime
import channels
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Group_Message(models.Model):
    user = models.CharField(max_length=10000)
    group_id=models.IntegerField()
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    dataURL = models.CharField(max_length=100000000)
    

class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    notification=models.TextField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
