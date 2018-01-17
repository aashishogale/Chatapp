from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import NewRegister
from .forms import RegisterForm


# Create your views here
def fillinform(request):
    if request.method=='POST':
       
        form=RegisterForm(request.POST)
        if form.is_valid():

            login_name=form.cleaned_data.get('username')
            login_password=form.cleaned_data.get('password')
            login_firstname=form.cleaned_data.get('firstname')
            login_last_name=form.cleaned_data.get('lastname')
            user=User.objects.create_user(login_name,password=login_password,first_name=login_firstname,last_name=login_last_name)
            user.save()
            return HttpResponseRedirect(reverse('register:login'))

def showform(request):
    
  
    
    form=RegisterForm()
    # template=loader.get_template('register/register.html')
    return render(request,'register/register.html',{'form':form})


def showLogin(request):
    
    form=RegisterForm()
    return render(request,'register/login.html',{'form':form})

def checklogin(request):
      if request.method=='POST':
       
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=authenticate(request,username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
            if user is not None:
                login(request,user)
            
                return HttpResponse('welcome')
    
      return HttpResponse('wrong password')
