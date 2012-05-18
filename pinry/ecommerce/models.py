from django.db import models
from pinry.pins.models import Pin 


class similarItems(models.Model):
    name = models.CharField(max_length=200)   
    image = models.ImageField(upload_to='similarItems/',default="http://www.seankenney.com/portfolio_images/Sculpture/Google/2.jpg")
    page_url = models.URLField(default="http://www.google.in")
    pins = models.ForeignKey(Pin,blank=True, null=True)
 

#class product(models.Model):
    #name = models.CharField(max_length=200)
    #similarItems = models.ForeignKey(similarItems)   
