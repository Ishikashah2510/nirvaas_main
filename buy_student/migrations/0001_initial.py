# Generated by Django 3.1.3 on 2020-11-20 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sell_staff', '0001_initial'),
        ('welcome', '0002_auto_20201120_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_quantity', models.IntegerField(default=0)),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_id', to='sell_staff.items')),
                ('Item_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_price', to='sell_staff.items')),
                ('Item_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_title', to='sell_staff.items')),
                ('buyer_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welcome.users')),
            ],
        ),
    ]
