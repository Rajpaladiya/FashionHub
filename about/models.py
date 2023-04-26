from django.db import models

class about_us(models.Model):
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)

    Description=models.CharField(max_length=10000)
    image=models.ImageField(upload_to='static/about')

class Footer(models.Model):
    Address=models.CharField(max_length=600)
    telephone=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
