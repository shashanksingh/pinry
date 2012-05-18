from django.db import models
from pinry.pins.models import Pin 


class similarItems(models.Model):
    name = models.CharField(max_length=200)   
    #image = models.ImageField(upload_to='pins/pin')
    image = models.URLField(default="http://upload.wikimedia.org/wikipedia/en/b/bc/Wiki.png")
    page_url = models.URLField(default="http://www.google.in")
    pins = models.ForeignKey(Pin,blank=True, null=True)
 

#class product(models.Model):
    #name = models.CharField(max_length=200)
    #similarItems = models.ForeignKey(similarItems)   
