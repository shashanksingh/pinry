from django.db import models
from pinry.pins.models import Pin 


class similarItems(models.Model):
    name = models.CharField(max_length=200)   
    image = models.ImageField(upload_to='pins/pin')
    page_url = models.URLField()
    pins = models.ForeignKey(Pin)
 

#class product(models.Model):
    #name = models.CharField(max_length=200)
    #similarItems = models.ForeignKey(similarItems)   
