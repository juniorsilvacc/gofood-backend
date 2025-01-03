# Generated by Django 5.1.2 on 2024-11-01 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='maximum',
        ),
        migrations.RemoveField(
            model_name='additional',
            name='minimum',
        ),
        migrations.AddField(
            model_name='additional',
            name='quantity_options',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3, 'O máximo é 3')]),
        ),
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
