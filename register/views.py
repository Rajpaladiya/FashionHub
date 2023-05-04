from django.shortcuts import render
from .models import REGISTER

def sign_up(request):
    
    if(request.GET.get('Username') and request.GET.get('Email') and request.GET.get('Password')):
        USERNAME=request.GET.get('Username')
        EMAIL= request.GET.get('Email')
        PASSWORD=request.GET.get('Password')
        REGISTER.objects.create(Username=USERNAME,Email=EMAIL,Password=PASSWORD)
        r=REGISTER.objects.all()
        print("yuadcgosdcidscsdh",r)

    return render(request,('account.html'))
                
                
             
