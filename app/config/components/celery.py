import os

CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_BROKER_URL = f'{os.getenv("CELERY_BROKER_URL")}'
CELERY_TIMEZONE = "Europe/Moscow"
