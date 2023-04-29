from os import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = environ.get('DEBUG', False) == 'True'

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = ['mailer/locale']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'


EVENT_API_BULK_MAILS = 'notifications_event_api:8001/api/v1/events/send-bulk_mails'
EVENT_API_ONE_MAIL = 'notifications_event_api:8001/api/v1/events/send-mail'

