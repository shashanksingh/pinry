from django.conf.urls import patterns, include, url
from .api import PinResource

pin_resource = PinResource()

urlpatterns = patterns('',
    url(r'^pins/recent/(?P<page>\d*)/$', 'pinry.api.views.pins_recent', name='pins-recent'),
    url(r'^pins/user/recent/(?P<user_id>\d*)/(?P<page>\d*)/$', 'pinry.api.views.pins_user_recent', name='pins-user-recent'),
    url(r'^pins/add/$','pinry.api.views.pins_add',name='pins-add'),
    url(r'^pins/add/form/$','pinry.api.views.pins_add_form',name='pins-add-form'),
    url(r'', include(pin_resource.urls)),
)
