from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('pinry.core.urls', namespace='core')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'^api/', include('pinry.api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ecommerce/',include('pinry.ecommerce.urls', namespace='ecommerce')),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),  
    url(r'^pages/$',include('pinry.flatpages.urls',namespace='flatpages')),
    url(r'^robots\.txt$', 'django.views.generic.simple.direct_to_template',{'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^humans\.txt$', 'django.views.generic.simple.direct_to_template',{'template': 'humans.txt', 'mimetype': 'text/plain'}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',{'url': '/media/img/favicon.ico'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
