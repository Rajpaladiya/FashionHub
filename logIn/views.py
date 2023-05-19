from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from .models import student
from django.contrib.auth import authenticate,login as login


      

def log_in(request):
    
    if request.method == 'POST':
        login_user=request.POST.get("Username")
        login_password=request.POST.get("Password")
        user=authenticate(request,username=login_user,password=login_password)
        print(user)
        # login(request,user)
        # print("sucess")
        # return redirect('/')

        

    return render(request,'login.html') 

# Create your views here.
