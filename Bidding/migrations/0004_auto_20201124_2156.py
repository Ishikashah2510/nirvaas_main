# Generated by Django 3.1.3 on 2020-11-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bidding', '0003_auto_20201124_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid_items',
            name='seller_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='buyer_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='seller_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
