from django.db import models
from categories.models import Category


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    addition = models.FloatField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Additional(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    maximum = models.IntegerField()
    minimum = models.IntegerField()
    options = models.ManyToManyField(Option)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.CharField(max_length=2000)
    additionals = models.ManyToManyField(Additional, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
