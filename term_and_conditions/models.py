from django.db import models

class TERM(models.Model):
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    condition=models.CharField(max_length=1000)

class Footer(models.Model):
    Address=models.CharField(max_length=600)
    telephone=models.CharField(max_length=200)
    email=models.CharField(max_length=100) 

