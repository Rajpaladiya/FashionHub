from django.shortcuts import render
from .models import contact
from .models import contact_about

def contact_page(request):

    contact_about_i=contact_about.objects.all()

    if(request.GET.get('name') and request.GET.get('email') and request.GET.get('subject') and request.GET.get('message')):
        NAME=request.GET.get('name')
        EMAIL=request.GET.get('email')
        SUBJECT=request.GET.get('subject')
        MESSAGE=request.GET.get('message')
        contact.objects.create(Name=NAME,Email=EMAIL,Subject=SUBJECT,Message=MESSAGE)
        c=contact.objects.all()
        print(c)
        
        

    return render(request,('contact.html'),{'Contact_About':contact_about_i})
    

# Create your views here.
