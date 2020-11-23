from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='D:/codes/python_codes/nirvaas_main/media/')
# Create your models here.
class Items(models.Model):
    Item_id = models.IntegerField(primary_key=True)
    Item_title = models.CharField(max_length=100)
    Item_ab = models.CharField(default="", max_length=100)
    Item_price = models.FloatField()
    Item_quantity = models.IntegerField(max_length=2)
    Item_description = models.CharField(max_length=1000, default="")
    Item_photo = models.ImageField(storage=fs)
    Item_type = models.CharField(max_length=20)
