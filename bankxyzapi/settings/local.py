from bankxyzapi.settings.base import *

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '061299victor',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}