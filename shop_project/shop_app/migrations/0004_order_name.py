# Generated by Django 5.0.6 on 2024-07-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Default Name', max_length=50),
        ),
    ]
