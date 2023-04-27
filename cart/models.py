from django.db import models
class add_to_cart(models.Model):
    product_name=models.CharField('name',max_length=100)
    product_price=models.CharField('price',max_length=100)
    product_Quantity=models.CharField('Quantity',max_length=100)
    
