from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Users(models.Model):
    name = models.CharField(max_length=60)
    mobile_no = models.IntegerField(max_length=10, unique=True)
    type_user = models.CharField(max_length=20)
    email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)


class Notification(models.Model):
    email_id = models.EmailField(max_length=50)
    notification = models.CharField(max_length=100)
    nid = models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, default=datetime.now)

