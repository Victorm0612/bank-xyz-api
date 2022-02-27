from email.policy import default
from bankxyzapi.settings.base import *
import dj_database_url
from decouple import config

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

## Override base.py settings here
DATABASES = {
    'default': dj_database_url.config(
      default=config('DATABASE_URL')
    )
}

try:
  from bankxyzapi.settings.local import *
except:
  pass