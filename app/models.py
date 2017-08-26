from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    sku = models.IntegerField(unique=True)
    source = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    product_type = models.CharField(max_length=200)
    mrp = models.IntegerField()

    
