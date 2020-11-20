from django.db import models
from sell_staff import models as smd
from welcome import models as wmd

# Create your models here.
class Cart(models.Model):
    Item_id = models.ForeignKey(smd.Items, on_delete=models.CASCADE)
    Item_title = models.ForeignKey(smd.Items, on_delete=models.CASCADE)
    Item_price = models.ForeignKey(smd.Items, on_delete=models.CASCADE)
    Item_quantity = models.IntegerField(default=0)
    buyer_email = models.ForeignKey(wmd.Users,on_delete=models.CASCADE())
