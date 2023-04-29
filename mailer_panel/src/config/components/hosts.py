from os import environ

DEBUG = environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['*']
CORS_ALLOWED_ORIGINS = ['*']
