from django.db import models

# Create your models here.


class Cart(models.Model):
    Item_id = models.IntegerField(default=0)
    Item_title = models.CharField(max_length=100)
    Item_price = models.FloatField()
    Item_quantity = models.IntegerField(max_length=2, default=1)
    email_id = models.EmailField(default="")
    Order_id = models.IntegerField(primary_key=True, default=111)


class Order(models.Model):
    Item_id = models.IntegerField(default=0)
    Item_title = models.CharField(max_length=100)
    Item_price = models.FloatField()
    Item_quantity = models.IntegerField(max_length=2, default=1)
    email_id = models.EmailField(default="")
    Order_id = models.IntegerField(default=111)
    Order_date = models.DateField(default='2000-10-05')
