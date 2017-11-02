"""GO_KART URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import homepage

from Accounts.views import login_view, logout_view, register_view, auth_view
from Seller.views import AddProduct, results
from Orders.views import orders, Display_Orders, Delete_Order
from django.conf import settings
from django.conf.urls.static import static
from Cart.views import Cart_Items, Cart_delete, cart
from Redirect.views import redirect
app_name = 'GO_KART'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name = 'homepage'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^auth/$', auth_view, name='authenticate'),
    url(r'^register/$', register_view, name='register'),
    url(r'^sell-item/$', AddProduct.as_view(), name = 'AddProduct'),
    url(r'^selling-items/', include('Seller.urls')),
    url(r'^results/$', results, name = 'query_result'),
    url(r'^cart/', include('Cart.urls')),
    url(r'redirect/(?P<Seller>[A-Za-z]+)/(?P<Product_Name>[A-Za-z0-9]+)/$', include('Redirect.urls')),
    url(r'^orders/(?P<Username>[a-zA-Z0-9_.-]+)/(?P<pk>[0-9]+)/add/$', orders, name = 'Orders'),
    url(r'^orders/(?P<Username>[a-zA-Z0-9_.-]+)/$', Display_Orders, name = 'Display-Orders'),
    url(r'^orders/(?P<pk>[0-9]+)/delete/$', Delete_Order, name = 'Delete-Order'),
    #url(r'redirect/(?P<Seller>[a-zA-Z])/(?P<Product_Name>[a-zA-Z0-9]+)/$', redirect, name = 'redirect'),

]
if settings.DEBUG:              #True if in development mode
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)