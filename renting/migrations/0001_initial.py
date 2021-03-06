# Generated by Django 3.1.3 on 2021-01-02 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentItems',
            fields=[
                ('rent_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('item_name', models.CharField(default='', max_length=255)),
                ('item_ab', models.CharField(default='', max_length=255)),
                ('item_type', models.CharField(default='', max_length=200)),
                ('item_description', models.CharField(default='', max_length=255)),
                ('item_photo', models.ImageField(upload_to='rentmedia/')),
                ('renter_name', models.CharField(default='', max_length=255)),
                ('rent_var', models.BooleanField(default=False)),
                ('rent_date', models.DateTimeField(default=datetime.datetime.now)),
                ('rented_until', models.DateTimeField(default=datetime.datetime(2021, 4, 2, 20, 38, 47, 644697))),
            ],
        ),
    ]
