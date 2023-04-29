from os import environ

DEBUG = environ.get('DEBUG', False) == 'True'
ALLOWED_HOSTS = ['*']
