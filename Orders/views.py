# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Seller.models import ProductDescription
from django.shortcuts import render
from .models import Orders
def orders(request, pk, Username):
    product = ProductDescription.objects.get(pk=pk)
    to_add = Orders()
    Username =  request.user.username
    Username = Username
    to_add.User = Username
    to_add.pk = product.pk
    to_add.Product_Image = product.Product_Image
    to_add.Seller_Username = product.Seller_Username
    to_add.Price = product.Price
    to_add.Product_Name = product.Product_Name
    to_add.Company_Name = product.Company_Name
    to_add.Category = product.Category
    to_add.save()
    data = Orders.objects.all()
    return render(request, 'Orders/Orders.html', {'data': data})
def Display_Orders(request, Username):
    products = Orders.objects.filter(User = Username)
    return render(request, 'Orders/Orders.html', {'data': products})
def Delete_Order(request, pk):
    product = Orders.objects.get(pk=pk)
    product.delete()
    products = Orders.objects.filter(User = request.user.username)
    return render(request, 'Orders/Orders.html', {'data': products})

# Create your views here.
