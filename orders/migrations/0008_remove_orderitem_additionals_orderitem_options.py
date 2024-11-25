# Generated by Django 5.1.2 on 2024-11-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_total_value'),
        ('products', '0004_remove_additional_maximum_remove_additional_minimum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='additionals',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='options',
            field=models.ManyToManyField(blank=True, to='products.option'),
        ),
    ]