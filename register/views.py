from django.shortcuts import render

    
from django.http import HttpResponse
from django.template import loader
from .models import NewRegister
    
# Create your views here
def fillinform(request):
    login_name=request.POST.get('name')
    login_password=request.POST.get('password')
    model_register=NewRegister( login_name= login_name, login_password= login_password)
    model_register.save()
    return HttpResponse("you are successful")

def showform(request):
    
    context={}
    template=loader.get_template('register/register.html')
    return  HttpResponse(template.render(context,request))


def showLogin(request):
    context={}
    template=loader.get_template('register/login.html')
    return  HttpResponse(template.render(context,request))

def checklogin(request):
    qset=NewRegister.users.all()

    for user in qset:
        if user.login_name==request.GET.get('name') and user.login_password==request.GET.get('password'):
            return HttpResponse("welcome")
    
    return HttpResponse('wrong password')
