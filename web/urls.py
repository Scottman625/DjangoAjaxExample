from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('index', views.index, name = 'index'), 
    path('ajax_refresh_county', views.ajax_refresh_county, name = 'ajax_refresh_county'),
]