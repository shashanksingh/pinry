from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^pins/recent/(?P<page>\d*)/$', 'pinry.api.views.pins_recent', name='pins-recent'),
    url(r'^pins/add/$','pinry.api.views.pins_add',name='pins-add'),
    url(r'^pins/add/form/$','pinry.api.views.pins_add_form',name='pins-add-form'),
)
