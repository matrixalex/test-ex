from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from .models import Post
urlpatterns = [
    url(r'^edit-post/(?P<pk>\d+$)',views.editPost),
    url(r'^create-post/',views.createPost),
    url(r'^create',views.create),
    url(r'^edit/',views.edit),
    url(r'(?P<pk>\d+$)', views.showPost),
    url(r'^$',views.showAll),
]