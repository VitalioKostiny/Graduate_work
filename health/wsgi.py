"""
WSGI config for health project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from users.views import create_manager

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health.settings')

# create user with 'manager' role
create_manager()

application = get_wsgi_application()
