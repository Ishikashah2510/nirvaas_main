# Generated by Django 3.1.3 on 2020-11-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy_student', '0005_auto_20201124_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_date',
            field=models.DateField(default='2000-10-05'),
        ),
    ]
