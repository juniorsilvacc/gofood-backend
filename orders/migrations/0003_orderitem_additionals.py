# Generated by Django 5.1.2 on 2024-11-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_reference_remove_order_telephone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='additionals',
            field=models.TextField(blank=True),
        ),
    ]