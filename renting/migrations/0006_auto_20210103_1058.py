# Generated by Django 3.1.3 on 2021-01-03 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0005_auto_20210103_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitems',
            name='rented_until',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 10, 58, 4, 882902)),
        ),
    ]
