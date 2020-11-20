from django.db import models

# Create your models here.
class Bid_Items(models.Model):
    item_id = models.IntegerField(primary_key=True)
    seller_email = models.EmailField()
    threshold_value = models.FloatField()
    item_name = models.CharField()
    item_description = models.CharField(max_length = 1000, default='')
    item_photo = models.ImageField(upload_to='/Bid Item Pics/')

class Bidding(models.Model):
    item_id = models.ForeignKey(Bid_Items,primary_key=True, on_delete=models.CASCADE())
    seller_email = models.ForeignKey(Bid_Items, on_delete=models.CASCADE())
    buyer_email = models.EmailField()
    bid_value = models.FloatField()
    threshold_value = models.ForeignKey(Bid_Items, on_delete=models.CASCADE())