# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Seller.models import ProductDescription
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Cart
from django.shortcuts import render
def cart(request, username):
    product = ProductDescription.objects.get(pk=request.POST['Add_to_Cart'])
    to_add = Cart()
    to_add.User = username
    to_add.pk = product.pk
    to_add.Product_Image = product.Product_Image
    to_add.Seller_Username = product.Seller_Username
    to_add.Price = product.Price
    to_add.Product_Name = product.Product_Name
    to_add.Company_Name = product.Company_Name
    to_add.Category = product.Category
    to_add.save()
    data = Cart.objects.all()
    return render(request, 'Cart/Cart.html', {'data': data})
def Cart_Items(request, username):
    data = Cart.objects.filter(User = username)
    return render(request, 'Cart/Cart.html', {'data': data, 'username': username})
def Cart_delete(request, pk, username):
    data = Cart.objects.get(pk = pk)
    data.delete()
    data = Cart.objects.all()
    return render(request, 'Cart/Cart.html', {'data': data})



