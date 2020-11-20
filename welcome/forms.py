from django import forms
from welcome.models import Users
from django.contrib.auth.models import User


class Login(forms.Form):
    email = forms.EmailField(label='Email ID')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput,label='Password')
    CHOICES = [('1', 'Student'), ('2', 'Stationery Staff'),('3','Administrator')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class Registration(forms.Form):
    name = forms.CharField(max_length=60, label='Name')
    email = forms.EmailField(label='Email ID')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Re-enter Password')
    mobile_no = forms.IntegerField(min_value=6000000000, max_value=9999999999)
    CHOICES = [('1', 'Student'), ('2', 'Stationery Staff'), ('3', 'Administrator')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

