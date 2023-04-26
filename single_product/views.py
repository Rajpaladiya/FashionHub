from django.shortcuts import render
from .models import single
from .models import single_product_img
from .models import similar
from .models import recently


def single_product(request):
    single_i=single.objects.all()
    single_product_i=single_product_img.objects.all()
    similar_i=similar.objects.all()
    recently_i=recently.objects.all()
    return render(request,('single-product.html'),{'Single':single_i,'Single_Product':single_product_i,'Similar':similar_i,'Recently':recently_i})

# Create your views here.
