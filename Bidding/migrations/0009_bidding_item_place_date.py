# Generated by Django 3.1.3 on 2020-11-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bidding', '0008_auto_20201125_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='item_place_date',
            field=models.DateField(default='2000-10-05'),
        ),
    ]