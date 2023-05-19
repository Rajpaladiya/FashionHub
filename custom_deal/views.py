from django.shortcuts import render
from .models import shop_details
from .models import Footer
def deal(request):

    shop_details_i=shop_details.objects.all()
    Footer_i=Footer.objects.all()
    return render(request,('custom-deal-page.html'),{'shop':shop_details_i,'FOOTER':Footer_i})


