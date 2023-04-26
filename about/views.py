from django.shortcuts import render
from .models import about_us
from .models import Footer


def about(request):
    about_us_i=about_us.objects.all()

    footer=Footer.objects.all()

    return render(request,('about.html'),{'About':about_us_i,'FOOTER':footer})

# Create your views here.
