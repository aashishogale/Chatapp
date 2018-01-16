from django.db import models


# Create your models here.
class NewRegister(models.Model):
    login_name=models.CharField(max_length= 100)
    login_password=models.CharField(max_length= 100)
    chatfield=models.CharField(max_length= 100)
    users=models.Manager()
