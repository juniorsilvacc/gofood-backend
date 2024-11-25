from django.db import models
from categories.models import Category
from django.core.exceptions import ValidationError


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    addition = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.CharField(max_length=2000)
    options = models.ManyToManyField(Option, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        MAX_OPTIONS = 3

        if self.pk:
            if self.options.count() > MAX_OPTIONS:
                raise ValidationError(f"Um produto não pode ter mais que {MAX_OPTIONS} opções.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
