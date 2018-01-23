from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class UserActivity(models.Model):
    last_activity_ip = models.GenericIPAddressField()
    last_activity_date = models.DateTimeField(default = datetime(1950, 1, 1))
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)