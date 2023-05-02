from django.shortcuts import render
from .models import carousel_1
from .models import carousel_2
from .models import carousel_3
from .models import banner
from .models import men_latest
from .models import men_top_rating
from .models import men_hot_deals
from .models import men_banner
from .models import women_latest
from .models import women_top_rating
from .models import toys_latest
from .models import toys_top_rating
from .models import mobiles_tablets
from .models import smartwatches
from .models import consumer_electronics
from .models import tv
from .models import books
from .models import single
from .models import single_product


def index(request):

    # **********************************MEN SECTION**********************************
    carousel_one = carousel_1.objects.all()
    # print(carousel_one)

    carousel_two = carousel_2.objects.all()
    # print(carousel_two)

    carousel_three = carousel_3.objects.all()
    # print(carousel_three)

    banner_i = banner.objects.all()
    # print(banner_i)

    men_latest_i = men_latest.objects.all()
    # print(men_latest_i)


    # wishlists = wishlitst.objects.all()
   

    

    men_top_rating_i = men_top_rating.objects.all()
    # print(men_top_rating_i)

    men_hot_deals_i = men_hot_deals.objects.all()
    # print(men_hot_deals)

    men_banner_i = men_banner.objects.all()
    # print(men_banner_i)

    # ********************************WOMEN SECTION************************************************

    women_latest_i = women_latest.objects.all()
    # print(women_latest_i)

    women_top_rating_i=women_top_rating.objects.all()
    # print(women_top_rating_i)


# **************************************TOYS SECTION***************************************************
    toys_latest_i=toys_latest.objects.all()
    # print(toys_latest_i)

    toys_top_rating_i=toys_top_rating.objects.all()
    # print(toys_top_rating_i)

# **********************************Mobiles & Tablets****************************************************
    mobiles_tablets_i=mobiles_tablets.objects.all()
    # print(mobiles_tablets_i) 

    smartwatches_i=smartwatches.objects.all()
    # print(smartwatches_i)
# ***********************************consumer_electronics******************************************
    consumer_electronics_i=consumer_electronics.objects.all()
    # print(consumer_electronics)

    tv_i=tv.objects.all()
    # print(tv_i)

#**************************************BOOKS SECTION**************************************
    books_i=books.objects.all()
    # print(books_i)

    single_i=single.objects.all()

    single_product_i=single_product.objects.all()
    

    return render(request, ('home.html'), {'carousel_image1': carousel_one, 'carousel_image2': carousel_two, 'carousel_image3': carousel_three, 'Men_Latest': men_latest_i, 'Banner': banner_i, 'Men_Top_rating': men_top_rating_i, 'Men_Hot_Deals': men_hot_deals_i, 'Men_Banner': men_banner_i, 'Women_Latest': women_latest_i, 'Women_Top_Rating':women_top_rating_i,'Toys_Latest':toys_latest_i,'Toys_Top_Rating':toys_top_rating_i,'Mobiles_Tablets':mobiles_tablets_i,'Smartwatches':smartwatches_i,'Consumer_Electronics':consumer_electronics_i,"TV":tv_i,'Books':books_i,'Single':single_i,'Single_Product':single_product_i})
