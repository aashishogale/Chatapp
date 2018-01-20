from django.db import models


# Create your models here.


class ChatMessages(models.Model):
    message = models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    showmessage=models.Manager()