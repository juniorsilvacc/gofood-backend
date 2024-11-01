from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from products.models import Product
from django.core.validators import MinValueValidator


class Coupon(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=8, unique=True)
    discount = models.FloatField()
    uses = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    zip_code = models.CharField(max_length=8, blank=True)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    district = models.CharField(max_length=50, blank=True)
    reference = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Zip Code {self.zip_code}'


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('CREDIT_CARD', 'Cartão de Crédito'),
        ('DEBIT_CARD', 'Cartão de Débito'),
        ('PAYPAL', 'PayPal'),
        ('BANK_TRANSFER', 'Transferência Bancária'),
        ('CASH', 'Dinheiro'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    change_due = models.CharField(blank=True, max_length=20)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    date = models.DateTimeField(default=datetime.now)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(1, 'O valor não pode ser menor que R$ 1.0')
        ]
    )
    price = models.FloatField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Order Item {self.id} - {self.product.name} x {self.quantity}'
