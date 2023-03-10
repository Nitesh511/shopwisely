from django.db import models
from django.core.validators import *
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200,null=True,validators=[validators.MinLengthValidator(2)])
    category_descripation = models.TextField(null=True)
    category_image = models.ImageField(upload_to='static/uplods',null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to='static/uplods')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
    )
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    total_price = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, default='Pending')
    payment_method = models.CharField(max_length=200, choices=PAYMENT, null=True)
    payment_status = models.BooleanField(default=False, null=True, blank=True)
    contact_no = models.CharField(validators=[MinLengthValidator(9), MaxLengthValidator(10)], null=True, max_length=10)
    contact_address = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)