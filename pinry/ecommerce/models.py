from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=200)
    product_page = models.URLField()

class similarItems(models.Model):
    pass
		
