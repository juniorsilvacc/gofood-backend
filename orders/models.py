from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from products.models import Product, Option
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
    total_value = models.FloatField(default=0)
    change_due = models.CharField(blank=True, max_length=20)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    date = models.DateTimeField(default=datetime.now)
    delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        total_items = sum(item.get_total_price() for item in self.order_items.all())
        if self.coupon:
            total_items -= self.coupon.discount
        return max(total_items, 0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Salva o objeto e atribui um ID

        total_value = sum(item.get_total_price() for item in self.order_items.all())  # Calcula o valor total

        if self.coupon:
            total_value -= self.coupon.discount  # Aplica o desconto do cupom

        if total_value < 0:
            total_value = 0  # Impede que o valor total fique negativo

        self.total_value = total_value
        super().save(update_fields=["total_value"])  # Atualiza o total_value no banco de dados

    def __str__(self):
        return f"Order {self.id} - Total: {self.total}"


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(1, 'A quantidade não pode ser menor que 1')
        ]
    )
    options = models.ManyToManyField(Option, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price(self):
        return self.product.price

    @property
    def description(self):
        return self.product.description

    def get_total_price(self):
        # Calcula o preço base do produto multiplicado pela quantidade
        total_price = self.product.price * self.quantity
        
        # Adiciona o preço de cada opção selecionada
        options_total = sum(option.addition for option in self.options.all())
        
        # Soma o preço total das opções ao total do produto
        total_price += options_total
        
        return total_price

    def __str__(self) -> str:
        return f'Order Item {self.id} - {self.product.name} x {self.quantity}'
