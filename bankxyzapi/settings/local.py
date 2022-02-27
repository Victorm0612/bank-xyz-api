from bankxyzapi.settings.base import *
from decouple import config

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('NAME_LOCAL'),
        'USER': config('USER_LOCAL'),
        'PASSWORD': config('PASSWORD_LOCAL'),
        'HOST': config('HOST_LOCAL'),
        'PORT': config('PORT_LOCAL'),
    }
}