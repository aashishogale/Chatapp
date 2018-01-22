from django.conf.urls import url, include
from django.contrib import admin

from . import views
from django.urls import path
app_name="register"
urlpatterns=[
    path('register',views.showform,name='register'),
    path('enter',views.fillinform,name='enter'),
    path('loginpage',views.showLogin,name='login'),
    path('checklogin',views.checklogin,name='checklogin'),
    path('logout',views.logout_view,name='logout')
  
]