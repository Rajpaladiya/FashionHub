from django.db import models


class shop_details(models.Model):
     product=models.ImageField(upload_to='static/shop')  
     name=models.CharField(max_length=50)
     Description=models.CharField(max_length=1000)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     special=models.CharField(max_length=20)

class Footer(models.Model):
    Address=models.CharField(max_length=600)
    telephone=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
# Create your models here.
