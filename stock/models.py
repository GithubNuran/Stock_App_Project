from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, related_name = 'products')
    brand = models.ForeignKey(Brand, on_delete = models.SET_NULL, null = True, related_name = 'brand_products')
    stock = models.SmallIntegerField(blank = True, null = True, default = 0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Firm (models.Model):
    name = models.CharField(max_length=50, unique = True)
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    image = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete = models.CASCADE, related_name = 'purchases')
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'brand_purchasess')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'product_purchases')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits = 6 ,decimal_places = 2)
    price_total = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.product} {self.quantity}"

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name = 'brand_sales')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'product_sales')
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits = 6 ,decimal_places = 2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.product} {self.quantity}"
    





