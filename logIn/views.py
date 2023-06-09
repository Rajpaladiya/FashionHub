from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
def login_user(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user.id'] = user.id
            request.session['user.username'] = user.username

            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')


