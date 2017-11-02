from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import ProductDescription
from django.shortcuts import render_to_response
flag = False
class AddProduct(CreateView):
    model = ProductDescription
    fields = ['Category', 'Product_Name', 'Company_Name', 'Price', 'Product_Image', ]
    def form_valid(self, form):
        user = self.request.user
        form.instance.Seller_Username = user
        return super(AddProduct, self).form_valid(form)
def selling_items(request):
    Seller = request.user
    object = ProductDescription.objects.filter(Seller_Username=Seller)
    return render(request, 'Seller/SellingItems.html', {'items': object,})
def results(request):
    query = request.GET.get('q').strip()
    if (query == ''):
        return redirect('/')
    if(query.lower() == 'all'):
        data = ProductDescription.objects.all().order_by('Price')
        return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
    for check in ProductDescription.objects.all():
        if(check.Product_Name.lower() == query.lower()):
            data = ProductDescription.objects.filter(Product_Name = query).order_by('Price')
            return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
        elif(check.Category.lower() == query.lower()):
            data = ProductDescription.objects.filter(Category=query).order_by('Price')
            return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
        elif(check.Company_Name.lower() == query.lower()):
            data = ProductDescription.objects.filter(Company_Name=query).order_by('Price')
            return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
        elif(check.Seller_Username.lower() == query.lower()):
                data = ProductDescription.objects.filter(Seller_Username=query).order_by('Price')
                return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
        elif(check.Additional_Information.lower() == query.lower()):
                data = ProductDescription.objects.filter(Additional_Information=query).order_by('Price')
                return render(request, 'Seller/SearchBar.html', {'object': data, 'query': query})
    return render(request, 'Seller/NoItem.html', {'object': query})
def Delete_Selling_Item(request, pk, Seller):
    object = ProductDescription.objects.get(pk = pk)
    object.delete()
    object = ProductDescription.objects.filter(Seller_Username = Seller)
    return render(request, 'Seller/SellingItems.html', {'items': object, 'Seller': Seller})

# Create your views here.
