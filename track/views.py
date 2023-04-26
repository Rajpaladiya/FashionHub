from django.shortcuts import render
from .models import order_track
def Tracking(request):
    if(request.GET.get('orderid') and request.GET.get('email')):
     Orderid=request.GET.get('orderid')
     Email=request.GET.get('email')
     order_track.objects.create(order_id=Orderid,E_mail=Email)
     T=order_track.objects.all().values()
     print(T)
     

     return render(request,('track-order.html'))

# Create your views here.
