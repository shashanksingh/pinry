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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
