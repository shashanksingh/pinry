from django.utils import simplejson
from django.http import HttpResponse
from pinry.pins.models import Pin
from django.core.files import File
from django.core.files.images import ImageFile
from django.template.response import TemplateResponse
import urllib2
import hashlib

def pins_recent(request, page=1):
    start_pin = abs(int(page) - 1) * 25
    end_pin = int(page) * 25

    pins = Pin.objects.order_by('-id')[start_pin:end_pin]
    recent_pins = []
    for pin in pins:
        recent_pins.append({
            'id': pin.id,
            'thumbnail': pin.image.url.rstrip('.jpg')+".200x1000.jpg",
            'original': pin.image.url,
            'description': pin.description,
            'blog_url': pin.blog_url,
            'buy_url' : pin.buy_url,
        })

    return HttpResponse(simplejson.dumps(recent_pins), mimetype="application/json")

def pins_add_form(request):
    mediaBM=str(request.GET.get('media'))
    return HttpResponse("<html><body onload=\"window.resizeTo(600,600)\"><p><img src=\""+mediaBM+"\"/><br/><form action=\"/api/pins/add\"><input type=\"hidden\" name=\"media\" value=\""+mediaBM+"\" /><h2 style=\"font: normal 18px 'Lobster', cursive , bold; \">Describe what you like?</h2><br/><input type=\"textarea\" value=\"Like\" name=\"description\"style=\"width:200px; height: 40px;\"/><br/><br/><input type=\"submit\" style=\"background-color:#DFDFDF; \"/></form></p></body></html>")
    #return TemplateResponse(request, 'pins/new_pin_bookmarklet.html')

#FIXME: i am full of dirty hacks :(
def pins_add(request):
    mediaBM=str(request.GET.get('media'))
    #urlBM=str(request.GET.get('url'))
    descriptionBM=str(request.GET.get('description'))
    #titleBM=str(request.GET.get('title'))
    #is_videoBM=request.GET.get('is_video')
    nameHash = hashlib.sha224(mediaBM.split('/')[-1])
    nameOfMedia = "pins/pin/" + nameHash.hexdigest() + '.jpg'
    pinNew = Pin(url=mediaBM,description=descriptionBM,image=nameOfMedia)
    f_orig=open("/opt/sources/code/pinry/media/"+nameOfMedia,'w')
    f_thumbnail=open("/opt/sources/code/pinry/media/"+nameOfMedia.rstrip('.jpg')+".200x1000.jpg",'w')
    img_temp = ImageFile(f_orig)
    img_thumb_temp = ImageFile(f_thumbnail)
    temp_image = urllib2.urlopen(mediaBM).read()
    img_temp.write(temp_image)
    img_thumb_temp.write(temp_image)
    img_temp.flush()
    img_thumb_temp.flush()
    img_temp.close()
    img_thumb_temp.close()
    #img_temp.save(nameOfMedia)
    pinNew.save()
    return HttpResponse("<html><body onload=\"window.resizeTo(600,600)\"><p> <h2 style=\"font: normal 26px 'Lobster', cursive , bold;\" >Image Succesfully Loaded</h2><br/><img src=\""+mediaBM+"\"/><br/></p></body></html>")
