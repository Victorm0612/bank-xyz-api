"""
WSGI config for bankxyzapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("DJANGO_ENV") == 'prod':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankxyzapi.settings.prod')
elif os.environ.get("DJANGO_ENV") == 'dev':
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankxyzapi.settings.dev')
else:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankxyzapi.settings.local')

application = get_wsgi_application()
