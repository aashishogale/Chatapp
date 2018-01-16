from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns=[
    url(r'^register',views.showform,name='register'),
    url(r'^enter',views.fillinform,name='enter'),
    url(r'^loginpage',views.showLogin,name='login'),
    url(r'^checklogin',views.checklogin,name='checklogin'),
]