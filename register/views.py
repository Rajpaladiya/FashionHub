from django.shortcuts import render,redirect
from register.models import REGISTER
from django.contrib.auth.models import User 
from django.contrib import messages

def sign_up(request):
    
    if(request.POST.get('FirstName') and request.POST.get('LastName') and request.POST.get('Username') and request.POST.get('Email') and request.POST.get('Password')):
        FIRSTNAME=request.POST.get('FirstName')
        LASTNAME=request.POST.get('LastName')
        USERNAME=request.POST.get('Username')
        EMAIL= request.POST.get('Email')
        PASSWORD=request.POST.get('Password')
        

        user=User.objects.create(username=USERNAME,email=EMAIL,password=PASSWORD)
        user.first_name=FIRSTNAME
        user.last_name=LASTNAME
        user.save()
        messages.success(request,"Your Account Successfully  Created")
        return redirect('/login')
        
        
    # r=REGISTER.objects.all().values()
    # print(request.POST.get('Email'))

    return render(request,('register.html'))
                
                
             
