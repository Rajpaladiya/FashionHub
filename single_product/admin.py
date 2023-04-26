from django.contrib import admin
from .import models 

admin.site.register(models.single)
admin.site.register(models.single_product_img)
admin.site.register(models.similar)
admin.site.register(models.recently)

# Register your models here.
