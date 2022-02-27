from bankxyzapi.settings.base import *
from decouple import config

DEBUG = config('DEBUG_PROD', cast=bool)

ALLOWED_HOSTS = []

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('NAME_PROD'),
        'USER': config('USER_PROD'),
        'PASSWORD': config('PASSWORD_PROD'),
        'HOST': config('HOST_PROD'),
        'PORT': config('PORT_PROD'),
    }
}

try:
  from bankxyzapi.settings.local import *
except:
  pass