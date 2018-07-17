"""
WSGI config for redstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from mongoengine import connect

from django.core.wsgi import get_wsgi_application

connect("redstone")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redstone.settings")
application = get_wsgi_application()
