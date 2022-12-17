import os
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/', 'sqlite', 'db.sqlite3'),
        'TEST': {
            'NAME': 'ut_db',
        },
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
