# Generated by Django 3.1.3 on 2021-01-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_staff', '0005_auto_20210102_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_ab',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='Item_photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
