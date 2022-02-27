from bankxyzapi.settings.base import *
from decouple import config

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('NAME_DEV'),
        'USER': config('USER_DEV'),
        'PASSWORD': config('PASSWORD_DEV'),
        'HOST': config('HOST_DEV'),
        'PORT': config('PORT_DEV'),
    }
}

try:
  from bankxyzapi.settings.local import *
except:
  pass