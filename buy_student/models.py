from django.db import models
from sell_staff import models as smd
from welcome import models as wmd

# Create your models here.


class Cart(models.Model):
    Item_id = models.IntegerField(default=0)
    Item_title = models.CharField(max_length=100)
    Item_price = models.FloatField()
    Item_quantity = models.IntegerField(max_length=2, default=1)
    email_id = models.EmailField(default="")
    Order_id = models.IntegerField(primary_key=True, default=111)
