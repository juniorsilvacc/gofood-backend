# Generated by Django 5.1.2 on 2024-11-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='order',
            name='telephone',
        ),
        migrations.AddField(
            model_name='address',
            name='reference',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
