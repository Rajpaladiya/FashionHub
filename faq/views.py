from django.shortcuts import render
from .models import FAQ

def faq(request):
    FAQ_I=FAQ.objects.all()
    return render(('faq.html'),{'Faq':FAQ_I})

