from bankxyzapi.settings.base import *

## Override base.py settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfuo36c1rg4vqr',
        'USER': 'zqrbvndszuvnbu',
        'PASSWORD': '2e3314fc837fe83d4924f30001e1992f70ff78245ef31dd19bb0dc9ba13cb76b',
        'HOST': 'ec2-18-210-118-224.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

try:
  from bankxyzapi.settings.local import *
except:
  pass