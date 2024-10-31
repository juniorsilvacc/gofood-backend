# Generated by Django 5.1.2 on 2024-10-31 11:55

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_additional_created_at_additional_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zip_code', models.CharField(blank=True, max_length=8)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('district', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8, unique=True)),
                ('discount', models.FloatField()),
                ('uses', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('change_due', models.CharField(blank=True, max_length=20)),
                ('payment', models.CharField(choices=[('CREDIT_CARD', 'Cartão de Crédito'), ('DEBIT_CARD', 'Cartão de Débito'), ('PAYPAL', 'PayPal'), ('BANK_TRANSFER', 'Transferência Bancária'), ('CASH', 'Dinheiro')], max_length=20)),
                ('reference', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('telephone', models.CharField(max_length=30)),
                ('delivered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'O valor não pode ser menor que R$ 1.0')])),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
