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
    login_name=request.POST.get('name')
    login_password=request.POST.get('password')
    user=User.objects.create_user(login_name,password=login_password)
    user.save()
    return HttpResponseRedirect(reverse('register:login'))

def showform(request):
    
  
    
    form=RegisterForm()
    # template=loader.get_template('register/register.html')
    return render(request,'register/register.html',{'form':form})


def showLogin(request):
    
    context={}
    template=loader.get_template('register/login.html')
    return  HttpResponse(template.render(context,request))

def checklogin(request):
   user=authenticate(request,username=request.POST.get('name'),password=request.POST.get('password'))
   if user is not None:
       login(request,user)
  
       return HttpResponse('welcome')
    
   return HttpResponse('wrong password')
