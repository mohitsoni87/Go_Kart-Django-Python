# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
def redirect(request, Seller, Product_Name):
    Product_Name = Product_Name.split()
    Product_Name = ''.join(Product_Name)
    if(Seller == 'Flipkart'):
        link = 'https://' + str(Seller) + '.com/search?q=' + str(Product_Name)
        print(link)
        #return render(request, 'Seller/NoItem.html', {'data': link})
        return HttpResponseRedirect(link)
    elif(Seller == 'Amazon'):
        link = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + str(Product_Name)
        return HttpResponseRedirect(link)

# Create your views here.
