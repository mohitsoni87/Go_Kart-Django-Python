# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
class ProductDescription(models.Model):
    Seller_Username = models.CharField(max_length = 100, null = False)
    Category = models.CharField(max_length = 100, null = False)
    Company_Name = models.CharField(max_length = 100, null = False)
    Product_Name = models.CharField(max_length = 100, null = False)
    Price = models.CharField(max_length = 10, null = False)
    Additional_Information = models.CharField(max_length = 100, null = True)
    Product_Image = models.FileField(max_length=1000, null=True)
    def get_absolute_url(self):
        return reverse('Seller:SellingItems')
    def __str__(self):
        return self.Product_Name + ' - ' + self.Seller_Username

# Create your models here.
