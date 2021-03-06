from django.db import models


class BidItems(models.Model):
    item_id = models.IntegerField(primary_key=True)
    seller_email = models.EmailField(default="")
    threshold_value = models.FloatField()
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=1000, default='')
    item_photo = models.ImageField(upload_to='Bid Item Pics/')
    item_place_date = models.DateField(default='2000-10-05')


class Bidding(models.Model):
    item_id = models.IntegerField(primary_key=True)
    seller_email = models.EmailField(default="")
    item_name = models.CharField(max_length=1000, default='')
    buyer_email = models.EmailField(default='')
    prev_buyer_email = models.EmailField(default='')
    curr_bid_value = models.FloatField(default=0)
    prev_bid_value = models.FloatField(default=0)
    threshold_value = models.FloatField(default=0)
    old_bid_date = models.DateField(default='2000-10-05')
    new_bid_date = models.DateField(default='2000-10-05')
    item_place_date = models.DateField(default='2000-10-05')


class old_items_on_bid(models.Model):
    item_id = models.IntegerField(primary_key=True)
    seller_email = models.EmailField(default="")
    threshold_value = models.FloatField(default=0)
    last_bid_value = models.FloatField(default=0)
    buyer_email = models.EmailField(default="")
    bid_placed_on = models.DateField(default='2000-10-05')