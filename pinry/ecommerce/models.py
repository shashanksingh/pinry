from django.db import models
from pinry.pins.models import Pin 

# Create your models here.


class similarItems(models.Model):
    name = models.CharField(max_length=200)   
    image = models.ImageField(upload_to='pins/pin')
    page_url = models.URLField()
 

class product(models.Model):
    name = models.CharField(max_length=200)
    pins = models.ForeignKey(Pin)
    similarItems = models.ForeignKey(similarItems)   
