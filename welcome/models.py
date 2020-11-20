from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=60)
    mobile_no = models.IntegerField(max_length=10,unique=True)
    CHOICES = [('Student','Student'),('Stationery Staff','Stationery Staff'),('Administrator','Administrator')]
    type_user = models.CharField(max_length=20,choices=CHOICES)
    email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)

