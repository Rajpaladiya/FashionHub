from django.db import models

class FAQ(models.Model):
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    Description=models.CharField(max_length=10000)
    Question=models.CharField(max_length=700)
    Answer=models.CharField(max_length=700)

    
class Footer(models.Model):
    Address=models.CharField(max_length=600)
    telephone=models.CharField(max_length=200)
    email=models.CharField(max_length=100)