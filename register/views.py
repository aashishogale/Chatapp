from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from django.template import loader
from django.urls import reverse
from .models import ChatMessages,LoggedInUser
from .forms import RegisterForm, LoginForm
# from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.utils import timezone
import datetime



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
                logged=LoggedInUser(loggedinuser=user,status="NOT_LOGGED_IN")
                logged.save()
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
        

        if form.is_valid()  and  not request.session.session_key:
            print("hello agian")
            login_username=form.cleaned_data.get('login_username')
            print(login_username)
            login_password=form.cleaned_data.get('login_password')
            user = authenticate(request,username=login_username,password=login_password)
            print(form.cleaned_data.get('login_username'))
            print(form.cleaned_data.get('login_password'))
        
            chat=ChatMessages.showmessage.all()

            if user is not None:
                users=User.objects.all()
                login(request, user)
                request.session["logged_in"]="true"
                loguser=LoggedInUser.getusers.get(loggedinuser=request.user)
                loguser.status="LOGGED_IN"
                loguser.save()
                loggedinuserlist=User.objects.filter(loggedinuser__status="LOGGED_IN")
           
                return render(request,'register/welcome.html',{'name':user.username,'chatlist':chat,'users':users,'loggedinusers':loggedinuserlist})
                # return HttpResponse('welcome')

    return render(request, 'register/login.html', {'form': form})
    # return HttpResponse('wrong password')
@login_required
def logout_view(request):
    print(request.user)
    user=request.user
    print(user)
    loguser=LoggedInUser.getusers.get(loggedinuser=request.user)
    loguser.status="NOT_LOGGED_IN"
    loguser.save()
    logout(request)
    form = LoginForm()
   
    return redirect(reverse('register:login'))
