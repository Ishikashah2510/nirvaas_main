from django.db import models
from sell_staff import models as smd
from welcome import models as wmd

# Create your models here.


class Cart(models.Model):
    Item_id = models.ForeignKey(smd.Items, on_delete=models.CASCADE, related_name='Cart_id')
    Item_title = models.ForeignKey(smd.Items, on_delete=models.CASCADE, related_name='Cart_title')
    Item_price = models.ForeignKey(smd.Items, on_delete=models.CASCADE, related_name='Cart_price')
    Item_quantity = models.IntegerField(default=0)
    buyer_email = models.ForeignKey(wmd.Users, on_delete=models.CASCADE)
