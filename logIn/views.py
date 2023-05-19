from django.shortcuts import render
from .models import LOGIN
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login

def log_in(request):
    if(request.POST.get('Username') and request.POST.get('Password') ):
        USERNAME=request.POST.get('Username')
        PASSWORD=request.POST.get("Password")
        user=authenticate(request,username=USERNAME,password=PASSWORD)
        print(user)


    return render(request,'login.html') 
# Create your views here.
