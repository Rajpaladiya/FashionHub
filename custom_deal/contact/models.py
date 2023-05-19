from django.db import models

class contact(models.Model):
    Name=models.CharField(("name"), max_length=50)
    Email=models.CharField(('email'),max_length=100)
    Subject=models.CharField(('subject'),max_length=100)
    Message=models.CharField(('message'),max_length=500)

class contact_about(models.Model):
    Information=models.CharField(max_length=400)
    Location=models.CharField(max_length=500)
    Email=models.CharField(max_length=500)
    Telephone=models.CharField(max_length=100)
