# Generated by Django 5.0.6 on 2024-07-18 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_favourite_hari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite_hari',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.cart_hari'),
        ),
    ]
