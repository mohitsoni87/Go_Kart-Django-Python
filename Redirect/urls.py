from django.conf.urls import url
from .views import redirect
app_name = 'Redirect'
urlpatterns = [
    url(r'^$', redirect, name = 'redirect'),
]