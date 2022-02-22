from bankxyzapi.settings.base import *

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5u06cn7feed2d',
        'USER': 'itoszugkxpxqza',
        'PASSWORD': '9809217a50b0815cb70b9adc56e9665c3b9a55e7e08b098dab66515751923e70',
        'HOST': 'ec2-52-200-188-218.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

try:
  from bankxyzapi.settings.local import *
except:
  pass