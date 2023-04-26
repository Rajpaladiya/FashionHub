from django.shortcuts import render
from .models import section_name
from .models import section_one
from .models import section_two
from .models import section_three
from .models import section_four
from .models import section_five
from .models import section_six
from .models import section_seven
from .models import section_eight


def Directory(request):
    section_name_i=section_name.objects.all()

    section_one_i=section_one.objects.all()
    section_two_i=section_two.objects.all()
    section_three_i=section_three.objects.all()
    section_four_i=section_four.objects.all()
    section_five_i=section_five.objects.all()
    section_six_i=section_six.objects.all()
    section_seven_i=section_seven.objects.all()
    section_eight_i=section_eight.objects.all()
    

    




    return render(request,('store-directory.html'),{'Section_Name':section_name_i,'Section_One':section_one_i,'Section_Two':section_two_i,'Section_Three':section_three_i,'Section_Four':section_four_i,'Section_Five':section_five_i,'Section_Six':section_six_i,'Section_Seven':section_seven_i,'Section_Eight':section_eight_i})
# Create your views here.
