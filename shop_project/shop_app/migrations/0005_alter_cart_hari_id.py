# Generated by Django 5.0.6 on 2024-07-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_alter_favourite_hari_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_hari',
            name='id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
