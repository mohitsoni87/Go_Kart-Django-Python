from django.conf.urls import url, include
from . import views
app_name = 'Accounts'
urlpatterns = [url(r'^$', views.login_view, name ='login'),
               url(r'^loggedin/$', views.auth_view, name = 'authenticate'),
               url(r'^logout$', views.logout_view, name='logout'),
                   ]