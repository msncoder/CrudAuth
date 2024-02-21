from django.db import models
from  datetime import datetime,date
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=58,null=True)
    phone = models.CharField(max_length=11,null=True)
    email = models.EmailField()
    date_created = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=58,null=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('outdoor','outdoor')
    )
    name = models.CharField(max_length=58,null=True)
    price = models.FloatField()
    category = models.CharField(max_length=58,null=True,choices=CATEGORY)
    description = models.CharField(max_length=80,null=True,blank=True)
    date_created = models.DateField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=58,null=True,choices=STATUS)
