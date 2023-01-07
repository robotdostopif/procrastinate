import os
from procrastinate.settings.base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = [ 'kamelijoint.pythonanywhere.com', '127.0.0.1' ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEBUG = False

