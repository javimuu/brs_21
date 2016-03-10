__author__ = 'javimuu'

from . import base

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brs',
        'USER': 'javimuu',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}