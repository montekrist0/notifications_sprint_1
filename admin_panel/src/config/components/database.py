
from os import environ

DATABASES = {
    'default': {
        'ENGINE': environ.get('DB_ENGINE'),
        'NAME': environ.get('DB_NAME'),
        'USER': environ.get('DB_USER'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': environ.get('DB_HOST'),
        'PORT': environ.get('DB_PORT'),
    },
}