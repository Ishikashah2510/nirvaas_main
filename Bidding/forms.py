from django import forms
from welcome.models import Users
from django.contrib.auth.models import User
from Bidding.models import *

class Sell_Form(forms.Form):
    item_name = forms.CharField(label='Item Name')
    item_description = forms.CharField(max_length=1000, default='',label='Item Description')
    item_photo = forms.ImageField(label='Upload Photo of Item')
    threshold_value = forms.FloatField(label='Base Value')

class Make_Bid(forms.Form):
    bid_value = forms.FloatField(label='Enter Bid Value')