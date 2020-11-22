from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    name = models.CharField(max_length=60)
    mobile_no = models.IntegerField(max_length=10, unique=True)
    type_user = models.CharField(max_length=20)
    email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
