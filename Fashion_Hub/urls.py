"""Fashion_Hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views., name='')
Class-based views
    1. Add an import:  from other_app.views import 
    2. Add a URL to urlpatterns:  path('', .as_view(), name='')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('/',include('home.urls')),
    path('about',include('about.urls')),
    path('track',include('track.urls')),
    path('contact',include('contact.urls')),
    path('custom_deal',include('custom_deal.urls')),
    path('faq',include('faq.urls')),
    path('shop',include('shop.urls')),
    path('single_product',include('single_product.urls')),
    path('store_Directory',include('store_Directory.urls')),
    path('term_and_conditions',include('term_and_conditions.urls')),
    path('account',include('account.urls')),
    path('cart',include('cart.urls')),
    path('wishlist',include('wishlist.urls')),
    

    path('admin/', admin.site.urls),
]
