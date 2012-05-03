from pinry.settings import *

import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASE_ENGINE   = 'django.db.backends.mysql'
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_NAME = 'staging'
DATABASE_USER = 'staging'
DATABASE_PASSWORD = 'staging'

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE ,
        'NAME': DATABASE_NAME ,
	'HOST': DATABASE_HOST ,
	'PORT': DATABASE_PORT ,
	'USER': DATABASE_USER ,
	'PASSWORD': DATABASE_PASSWORD,
    }
}

SECRET_KEY = ''
