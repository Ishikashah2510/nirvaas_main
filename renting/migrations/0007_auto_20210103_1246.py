# Generated by Django 3.1.3 on 2021-01-03 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0006_auto_20210103_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitems',
            name='rented_until',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 12, 46, 32, 295000)),
        ),
    ]
