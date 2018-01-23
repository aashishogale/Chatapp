from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
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
from django.utils import timezone
import datetime
from channels import Group
import json
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from datetime import timedelta

from django.contrib.auth.models import User
from datetime import datetime, timedelta
from lastActivityDate.models import UserActivity

def get_online_users():
    fifteen_minutes = datetime.now() - timedelta(minutes=15)
    sql_datetime = datetime.strftime(fifteen_minutes, '%Y-%m-%d %H:%M:%S')
    users = UserActivity.objects.filter(last_activity_date__gte=sql_datetime)
    print(users)
    return [u.user for u in users]

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
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        # print(sessions)
        uid_list = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            uid_list.append(data.get('_auth_user_id', None))
        loggedInUsers = User.objects.filter(id__in=uid_list)
        print(loggedInUsers)

        if form.is_valid()  and  not request.session.session_key:
            print("hello agian")
            login_username=form.cleaned_data.get('login_username')
            print(login_username)
            login_password=form.cleaned_data.get('login_password')
            user = authenticate(request,username=login_username,password=login_password)
            # print(form.cleaned_data.get('login_username'))
            # print(form.cleaned_data.get('login_password'))
        
            # chat=ChatMessages.showmessage.all()

            if user is not None:
                # users=User.objects.all()
                login(request, user)
                # request.session["logged_in"]="true"
                loguser=LoggedInUser.getusers.get(loggedinuser=request.user)
                loguser.status="LOGGED_IN"
                loguser.save()
                data['loggedin']=user.username
                
                # loggedinuserlist=User.objects.filter(loggedinuser__status="LOGGED_IN")
                return redirect(reverse('register:welcome'))
                # return render(request,'register/welcome.html',{'name':user.username,'chatlist':chat,'users':users,'loggedinusers':loggedinuserlist})
                # return HttpResponse('welcome')

    return render(request, 'register/login.html', {'form': form})
    # return HttpResponse('wrong password')

def welcome(request):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    # print(sessions)
    uid_list = []
    
    print(get_online_users())
    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        # print("loggedin",data.get('logged_in',True))
        uid_list.append(data.get('_auth_user_id', None))
    loggedInUsers = User.objects.filter(id__in=uid_list)
    users=User.objects.all()
    # print(loggedInUsers)
    chat=ChatMessages.showmessage.all()
    request.session["logged_in"]="true"
    loguser=LoggedInUser.getusers.get(loggedinuser=request.user)
    loguser.status="LOGGED_IN"
    loguser.save()
    # user_activity_objects = OnlineUserActivity.get_user_activities(timedelta(minutes=60))
    # users = (user for user in user_activity_objects)

   

               
 
    loggedinuserlist=User.objects.filter(loggedinuser__status="LOGGED_IN")
    # data={}
    # data['loggedin']=loggedinuserlist
    # message={'loggedin':data['loggedin']}
    # Group('chat').send({"text":json.dumps(message),},immediately=True)
    return render(request,'register/welcome.html',{'name':request.user.username,'chatlist':chat,'users':users,'loggedinusers':loggedinuserlist})

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
