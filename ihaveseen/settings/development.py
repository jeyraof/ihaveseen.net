from .base import *

DEBUG = True
SECRET_KEY = 'development'
ALLOWED_HOSTS += []
CDN_HOST = 'http://localhost:8080'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ihaveseen_development',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

