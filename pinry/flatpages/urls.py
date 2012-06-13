from django.conf.urls import patterns, url

urlpatterns = patterns('pinry.flatpages.views',
    url(r'^$','goodies',name='goodies'),
)
