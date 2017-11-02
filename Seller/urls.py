from django.conf.urls import url
from .views import selling_items, Delete_Selling_Item
app_name = 'Seller'
urlpatterns = [
    url(r'^$', selling_items, name = 'SellingItems'),
    url(r'^(?P<Seller>[a-zA-Z0-9_.-]+)/(?P<pk>[0-9]+)/delete/$', Delete_Selling_Item, name = 'Delete-Selling-Items'),
]