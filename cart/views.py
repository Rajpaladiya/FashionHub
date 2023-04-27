from django.shortcuts import render

from .models import add_to_cart


def cart(request):
    if(request.GET.get('name') and request.GET.get('price') and request.GET.get('Quantity')):
        NAME=request.GET.get('name')
        PRICE=request.GET.get('price')
        QUANTITY=request.GET.get('Quantity')
        a=add_to_cart.objects.all()
        print(a)