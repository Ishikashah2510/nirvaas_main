# Generated by Django 3.1.3 on 2020-11-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_student', '0003_auto_20201123_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Item_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Item_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Item_quantity',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Item_title',
            field=models.CharField(max_length=100),
        ),
    ]
