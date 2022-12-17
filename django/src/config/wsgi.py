"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from .define_module import setup_default_setting
from django.core.wsgi import get_wsgi_application

setup_default_setting()
application = get_wsgi_application()
