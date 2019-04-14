from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^login-page/',views.log),
    #url(r'auth/',include('loginsys.urls')),
    url(r'^logout/',views.logt),
    url(r'^registration-page/',views.registr,name = 'registration'),
    url(r'^login/',views.login),
    url(r'^registration/',views.registration,name = 'registration'),

]
