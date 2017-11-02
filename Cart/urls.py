from django.conf.urls import url
from .views import cart, Cart_Items, Cart_delete
app_name = 'Cart'
urlpatterns = [
    url(r'^(?P<username>[A-Za-z0-9_.-]+)/$', Cart_Items, name='Cart'),
    url(r'^(?P<username>[A-Za-z0-9_.-]+)/add/$', cart, name = 'add_to_cart'),
    url(r'^(?P<username>[A-Za-z0-9_.-]+)/(?P<pk>[0-9]+)/delete/$', Cart_delete, name = 'Cart_delete'),
]