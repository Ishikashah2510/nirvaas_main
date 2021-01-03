# Generated by Django 3.1.3 on 2021-01-03 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0004_auto_20210102_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldRentedItems',
            fields=[
                ('rent_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('item_name', models.CharField(default='', max_length=255)),
                ('item_photo', models.ImageField(upload_to='oldrentmedia/')),
                ('renter_email', models.EmailField(default='', max_length=255)),
                ('rent_date', models.DateTimeField(default=datetime.datetime.now)),
                ('returned_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='rentitems',
            name='rented_until',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 10, 27, 18, 189039)),
        ),
    ]