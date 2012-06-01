from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Pin
from .forms import PinForm


def recent_pins(request):
    return TemplateResponse(request, 'pins/recent_pins.html', None)

def user_pins(request):
    user_id=str(request.GET.get('user_id'))
    context = {
       'user_id':user_id
    }
    return TemplateResponse(request,  'pins/recent_user_pins.html', context )


def new_pin(request):
    if request.method == 'POST':
        form = PinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New pin successfully added.')
            return HttpResponseRedirect(reverse('pins:recent-pins'))
        else:
            messages.error(request, 'Pin did not pass validation!')
    else:
        form = PinForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, 'pins/new_pin.html', context)
