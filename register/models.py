from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class ChatMessages(models.Model):
    message = models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    showmessage=models.Manager()

class LoggedInUser(models.Model):
    loggedinuser = models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,null=True)
    getusers=models.Manager()
  