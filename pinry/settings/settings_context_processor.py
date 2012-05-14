from django.conf import settings

def branding(request):
    settings_dict = {
	'BRANDING_LOGO': settings.BRANDING_LOGO,
        'MEDIA_DIR' : settings.MEDIA_DIR,
        'APP_NAME' : settings.APP_NAME,
    }
    return settings_dict
