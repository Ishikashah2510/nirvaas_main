from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class RentItems(models.Model):
    rent_id = models.IntegerField(default=0, primary_key=True)
    item_name = models.CharField(default='', max_length=255)
    item_ab = models.CharField(default='', max_length=255)
    item_type = models.CharField(default='', max_length=200)
    item_description = models.CharField(default='', max_length=255)
    item_photo = models.ImageField(upload_to='rentmedia/')
    renter_email = models.EmailField(default='', max_length=255)
    rent_var = models.BooleanField(default=False)
    rent_date = models.DateTimeField(default=datetime.now)
    rented_until = models.DateTimeField(default=datetime.today() + timedelta(90))


class OldRentedItems(models.Model):
    rent_id = models.IntegerField(default=0, primary_key=True)
    item_name = models.CharField(default='', max_length=255)
    item_photo = models.ImageField(upload_to='oldrentmedia/')
    renter_email = models.EmailField(default='', max_length=255)
    rent_date = models.DateTimeField(default=datetime.now)
    returned_date = models.DateTimeField(default=datetime.now)
