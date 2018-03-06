from eduApi.settings.base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eduApi',
        'USER': 'root',
        'PASSWORD': 'testteam',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}