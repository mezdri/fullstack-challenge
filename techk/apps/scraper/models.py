# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class Categories(models.Model):

    name = models.CharField(max_length=20)

    
class Books(models.Model):

    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    thumbnail_url = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    stock = models.BooleanField()
    product_description = models.TextField()
    upc = models.CharField(max_length=30)
