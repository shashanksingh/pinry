from django.conf.urls import patterns, include, url

urlpatterns = patterns('pinry.ecommerce.views',
   url(r'^similar-items/$', 'similar_items', name='similar-items'),
) 
