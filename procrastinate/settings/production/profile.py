import os
from procrastinate.settings.base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('PROCRASTINATE_ALLOWED_HOSTS').split(',')
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST':os.environ.get('MYSQL_HOST')
        'PORT':os.environ.get('MYSQL_PORT'),
    }
}

DEBUG = False

