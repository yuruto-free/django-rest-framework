import os
from .base import *

ALLOWED_HOSTS = os.getenv('DJANGO_WWW_VHOST', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'charset': os.getenv('DB_CHARSET'),
            'collation': os.getenv('DB_COLLATION'),
        },
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
