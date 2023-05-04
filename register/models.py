from django.db import models

class REGISTER(models.Model):
    username=models.CharField(('Username'),max_length=100)
    email=models.EmailField(('Email'),max_length=100)
    password=models.CharField(('Password'),max_length=100)
# Create your models here.
