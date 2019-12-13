from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djtrumpprod',
        'USER': 'djtrumpuser',
        'PASSWORD': 'djtrump',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
