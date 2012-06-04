from django.conf.urls import patterns, include, url

urlpatterns = patterns('pinry.ecommerce.views',
   url(r'^similar-items/$', 'similar_items', name='similar-items'),
   url(r'^similar/(?P<pin_id>\d*)/(?P<page>\d*)/$', 'pins_similar_items', name='pins-similar'),
) 
