# Generated by Django 3.1.3 on 2021-01-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_staff', '0006_auto_20210102_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_photo',
            field=models.ImageField(upload_to=''),
        ),
    ]