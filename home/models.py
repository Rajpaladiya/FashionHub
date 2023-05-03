from django.db import models


class Main_Logo(models.Model):
     logo=models.ImageField(upload_to='static/index/logo')

class carousel_1(models.Model):
    carousel_img=models.ImageField(upload_to='static/index/carousel_image1')
    title=models.CharField(max_length=250)
    sub_title=models.CharField(max_length=250)

class carousel_2(models.Model):
    carousel_img=models.ImageField(upload_to='static/index/carousel_image2')
    title=models.CharField(max_length=250)
    sub_title=models.CharField(max_length=250)
    sub_sub_title=models.CharField(max_length=250)

class carousel_3(models.Model):
    carousel_img=models.ImageField(upload_to='static/index/carousel_image3')
    title=models.CharField(max_length=250)
    sub_title=models.CharField(max_length=250)  
    sub_sub_title=models.CharField(max_length=250)


class banner(models.Model):
    banner_img=models.ImageField(upload_to='static/index/banner_img')


class men_latest(models.Model):
    product=models.ImageField(upload_to='static/index/men_latest')  
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    mrp=models.CharField(max_length=10)
    category_one=models.CharField(max_length=100)
    category_two=models.CharField(max_length=100)
    special=models.CharField(max_length=20)
    category_three=models.CharField(max_length=100)


    



    

class men_top_rating(models.Model):
    product=models.ImageField(upload_to='static/index/men_top_rating')  
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    mrp=models.CharField(max_length=10)
    category_one=models.CharField(max_length=100)
    category_two=models.CharField(max_length=100)
    category_three=models.CharField(max_length=100)
    special=models.CharField(max_length=20)



class men_hot_deals(models.Model):
    product=models.ImageField(upload_to='static/index/men_hot_deals')  
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    mrp=models.CharField(max_length=10)
    category_one=models.CharField(max_length=100)
    category_two=models.CharField(max_length=100)
    category_three=models.CharField(max_length=100)

class men_banner(models.Model):
    banner=models.ImageField(upload_to='static/index/men_banner')    
        

class women_latest(models.Model):
     product=models.ImageField(upload_to='static/index/women_latest')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     special=models.CharField(max_length=20)
    






class women_top_rating(models.Model):
     product=models.ImageField(upload_to='static/women_top_rating')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     special=models.CharField(max_length=20)

class toys_latest(models.Model):
     product=models.ImageField(upload_to='static/toys_latest')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     special=models.CharField(max_length=20)

class toys_top_rating(models.Model):
     product=models.ImageField(upload_to='static/toys_top_rating')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     special=models.CharField(max_length=20)


class mobiles_tablets(models.Model):
     product=models.ImageField(upload_to='static/mobiles_tablets')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20)

class mobiles_tablets(models.Model):
     product=models.ImageField(upload_to='static/mobiles_tablets')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20)


class smartwatches(models.Model):
     product=models.ImageField(upload_to='static/smartwatches')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20)

class consumer_electronics(models.Model):
     product=models.ImageField(upload_to='static/consumer_electronics')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20) 
     
class tv(models.Model):
     product=models.ImageField(upload_to='static/tv')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20)  

class books(models.Model):
     product=models.ImageField(upload_to='static/books')  
     name=models.CharField(max_length=50)
     price=models.CharField(max_length=10)
     mrp=models.CharField(max_length=10)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     special=models.CharField(max_length=20)       

class single(models.Model):
     product=models.ImageField(upload_to='static/index/men_top_rating') 
     title=models.CharField(max_length=500)
     category_one=models.CharField(max_length=100)
     category_two=models.CharField(max_length=100)
     category_three=models.CharField(max_length=100)
     category_four=models.CharField(max_length=100)
     Description=models.CharField(max_length=900)
     price=models.CharField(max_length=100)
     mrp=models.CharField(max_length=100)
     Discount=models.CharField(max_length=100)
     Save=models.CharField(max_length=100)
     Only=models.CharField(max_length=100)
     Available_Color=models.CharField( max_length=100)
     Available_Size=models.CharField(max_length=100)     

class single_product(models.Model):
     product=models.ImageField(upload_to='static/index/men_top_rating') 