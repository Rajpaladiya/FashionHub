from django.db import models

class order_track(models.Model):
    order_id=models.CharField(('orderid'),max_length=100)
    E_mail=models.CharField(('email'),max_length=100)

# Create your models here.
