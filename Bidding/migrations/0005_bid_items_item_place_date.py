# Generated by Django 3.1.3 on 2020-11-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bidding', '0004_auto_20201124_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid_items',
            name='item_place_date',
            field=models.DateField(default='2000-10-05'),
        ),
    ]
