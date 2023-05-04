from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import login
from .models import signup


def Account(request):
        



      # USERNAME_S=request.GET.get('Username')
      # EMAIL_S=request.GET.get('Email')
      # PASSWORD_S=request.GET.get('Password')
      # USERNAME=request.GET.get('Username')
      # PASSWORD=request.GET.get('Password')

      # if(request.GET.get('Username') and request.GET.get('Email') and request.GET.get('Password')):

      #   USERNAME_S=request.GET.get('Username')
      #   EMAIL=request.GET.get('Email')
      #   PASSWORD_S=request.GET.get('Password')
      #   # filter with email
        
      #   checkUser = signup.objects.filter(Email=EMAIL).values()
      #   print(len(checkUser))
      #   if len(checkUser) != 0:
      #     return HttpResponse("User Already Exist") 
           
      #   signup.objects.create(Username=USERNAME_S,Email=EMAIL,Password=PASSWORD_S)
      #   S=signup.objects.all()
      #   print(S)
      #   return redirect('/')

      # if(request.GET.get('Username') and request.GET.get('Password')):

      #   USERNAME=request.GET.get('Username')
      #   PASSWORD=request.GET.get('Password')

      # f=login.objects.filter(Username=USERNAME,Password=PASSWORD).values()
      # print(f)
      # if len(f):
      #   return redirect('/')
      # else: 
      #   return HttpResponse("Password Wrong")
      
        # user=authenticate(request,Username=USERNAME,Password=PASSWORD)
        # print(user)
        # if user is not None:
        #     login(request, user)
        #     return redirect('/')
      
        # else:
        #      return HttpResponse(request,'ERROR')
        
        
        # L=login.objects.all()
        # # print(L)
        # if PASSWORD_S!=PASSWORD or USERNAME_S!=USERNAME:
        #     print("HELLO")
        #     return HttpResponse(request,'ERROR')
         
        #  return redirect('/')

    












    # if(request.GET.get('Username') and request.GET.get('Password')):
    #     USERNAME=request.GET.get('Username')
    #     PASSWORD=request.GET.get('Password')
    #     account_page.objects.create(Username=USERNAME,Password=PASSWORD)
    #     L=account_page.objects.all()
    #     print(L)
      
    



        return render(request,'account.html')
