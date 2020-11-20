from django import forms
from welcome.models import Users
from django.contrib.auth.models import User


class View_Details(forms.Form):
    name = forms.CharField(max_length=60, label='Name of User',required=False)
    email = forms.EmailField(label='Email ID of User',required=False)

class Delete_Account(forms.Form):
    email = forms.EmailField(label='Email ID of User')