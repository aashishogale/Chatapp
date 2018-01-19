from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from .models import NewRegister
from .forms import RegisterForm, LoginForm
# from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages



# Create your views here

def fillinform(request):
    if request.method == 'POST':
        print("hello")
        form = RegisterForm(request.POST)
        print("hel",form.is_valid(),form.errors)
        if form.is_valid():

            login_name = form.cleaned_data.get('username')
            login_password = form.cleaned_data.get('password')
            login_firstname = form.cleaned_data.get('firstname')
            login_last_name = form.cleaned_data.get('lastname')
            login_email = form.cleaned_data.get('email')
            try:
                user = User.objects.create_user(
                    login_name,
                    password=login_password,
                    first_name=login_firstname,
                    last_name=login_last_name,
                    email=login_email)
                user.save()
                messages.info(request,"you are successful")
                return redirect(reverse('register:login'))
            except IntegrityError :
                messages.warning(request,"user name or email already exists")
                return redirect(reverse('register:register'))
            except :
                messages.warning(request,"system error")
                return redirect(reverse('register:register'))
        else:
            messages.warning(request,"fill all details")
            return render(request, 'register/register.html', {'form': form})

def showform(request):

    form = RegisterForm()
   
    return render(request, 'register/register.html', {'form': form})


def showLogin(request):

    form = LoginForm()

    return render(request, 'register/login.html', {'form': form})


def checklogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        print("hello")
        print(form.errors)
        if form.is_valid(): 
            print("hello agian")
            login_username=form.cleaned_data.get('login_username')
            print(login_username)
            login_password=form.cleaned_data.get('login_password')
            user = authenticate(request,username=login_username,password=login_password)
            print(form.cleaned_data.get('login_username'))
            print(form.cleaned_data.get('login_password'))
            if user is not None:
                login(request, user)
                return render(request,'register/welcome.html',{'name':user.username})
                # return HttpResponse('welcome')

    return render(request, 'register/login.html', {'form': form})
    # return HttpResponse('wrong password')
