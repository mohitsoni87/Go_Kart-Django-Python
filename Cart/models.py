# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Cart(models.Model):
    User = models.CharField(max_length = 100, null = True)
    Seller_Username = models.CharField(max_length = 100, null = True)
    Category = models.CharField(max_length = 100, null = False)
    Company_Name = models.CharField(max_length = 100, null = False)
    Product_Name = models.CharField(max_length = 100, null = False)
    Price = models.CharField(max_length = 10, null = False)
    Product_Image = models.FileField(max_length=1000, null=True)
    def __str__(self):
        return self.Product_Name + ' - ' + self.Seller_Username
# Create your models here.
