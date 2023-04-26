from django.db import models

class single(models.Model):
    single_product=models.ImageField(upload_to='static/single_product')
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
    Key_Features=models.CharField(max_length=100)
    Sku=models.CharField(max_length=100)
    Main_Material=models.CharField(max_length=100)
    Color=models.CharField(max_length=100)
    Sleeves=models.CharField(max_length=100)
    Top_Fit=models.CharField(max_length=100)
    Print=models.CharField(max_length=100)
    Neck=models.CharField(max_length=100)
    Pieces_Count=models.CharField(max_length=100)
    Occasion=models.CharField(max_length=100)
    Shipping_Weight_kg=models.CharField(max_length=100)

class single_product_img(models.Model):
    single_product_image=models.ImageField(upload_to='static/single_product')

class similar(models.Model):
    similar_product=models.ImageField(upload_to='static/single_product')  
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    mrp=models.CharField(max_length=10)
    category_one=models.CharField(max_length=100)
    category_two=models.CharField(max_length=100)
    special=models.CharField(max_length=20) 

class recently(models.Model):
    similar_product=models.ImageField(upload_to='static/single_product')  
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    mrp=models.CharField(max_length=10)
    category_one=models.CharField(max_length=100)
    category_two=models.CharField(max_length=100)
    special=models.CharField(max_length=20) 



        



    
