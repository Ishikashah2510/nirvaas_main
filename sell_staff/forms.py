from django import forms
from welcome.models import Users
from django.contrib.auth.models import User
from sell_staff.models import *

class Sell_Staff_Form(forms.Form):
    Item_title = forms.CharField(max_length=100,label='Title of Item')
    Item_ab = forms.CharField(default="",label='Author/Brand')
    Item_price = forms.FloatField(label='Price')
    Item_quantity = forms.IntegerField(max_length=2,label='Quantity')
    Item_description = forms.CharField(max_length=1000, default="",label='Description')
    Item_photo = forms.ImageField(label='Add Photo of Item')
    CHOICES = [('1', 'New'), ('2', 'Old')]
    Item_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)