from django.shortcuts import render
from .models import TERM
from .models import Footer

def Term(request):
    term_i=TERM.objects.all()
    footer=Footer.objects.all()

    return render(request,('term-and-condition.html'),{'Term':term_i,'FOOTER':footer})
