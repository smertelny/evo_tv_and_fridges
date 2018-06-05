from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['tv-and-fridges.herokuapp.com']

SECRET_KEY = os.environ['DJANGO_SECRET']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['DJANGO_DB_HOST'],
        'NAME': os.environ['DJANGO_DB_NAME'],
        'PORT': os.environ['DJANGO_DB_PORT'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASS'],
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}
