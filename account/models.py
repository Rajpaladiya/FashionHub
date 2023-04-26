from django.db import models

class login(models.Model):
    Username=models.CharField(('Username'),max_length=100)
    Password=models.CharField(('Password'),max_length=100)


class signup(models.Model):
    Username=models.CharField(('Username'),max_length=100)
    Email=models.CharField(('Email'),max_length=100)
    Password=models.CharField(('Password'),max_length=100)
    
