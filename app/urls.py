from django.conf.urls import url
from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    url(r'^$',views.index,name='index'),
]