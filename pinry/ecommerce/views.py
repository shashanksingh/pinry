#Thu May 17 07:01:10 EDT
#This view will have specific function for ecommerce functionalities like 
#treating a pin like product and fidning similar items from  db
#this would obviosly needs admin support 

from django.utils import simplejson
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import  similarItems
from pinry.pins.models import Pin

def pins_similar_items(request, pin_id=1, page=1):
    start_pin = abs(int(page) - 1) * 25
    end_pin = int(page) * 25

    pinNeeded = similarItems.objects.filter(pins=pin_id)
    similar_pins = []
    for pin in pinNeeded:
        similar_pins.append({
            'id': pin.id,
            'thumbnail': pin.image,
            'original': pin.image,
            'description': pin.page_url,
        })

    return HttpResponse(simplejson.dumps(similar_pins), mimetype="application/json")

def similar_items(request):
    pinInQuery = int(request.GET.get('pin_id'))
    context = {
         'pin_id' : pinInQuery,
    }
    return TemplateResponse(request,'similar_items.html',context)
