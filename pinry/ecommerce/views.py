#Thu May 17 07:01:10 EDT
#This view will have specific function for ecommerce functionalities like 
#treating a pin like product and fidning similar items from  db
#this would obviosly needs admin support 

from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import  similarItems
from pinry.pins.models import Pin

def similar_items(request):
    pinInQuery = int(request.GET.get('pin_id'))
    pinNeeded = similarItems.objects.filter(pins=pinInQuery)
    #pinNeeded = Pin.objects.all()
    #context = {
    #    'image': pinNeeded.image ,
    #    'page_url' : pinNeeded.page_url,
    #}
    context = {
         'similar' : pinNeeded,
    }
    return TemplateResponse(request,'similar_items.html',context)
