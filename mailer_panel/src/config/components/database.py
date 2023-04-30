from os import environ

DATABASES = {
    'default': {
        'ENGINE': environ.get('DB_ENGINE'),
        'NAME': environ.get('POSTGRES_DB'),
        'USER': environ.get('POSTGRES_USER'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD'),
        'HOST': environ.get('POSTGRES_HOST'),
        'PORT': environ.get('POSTGRES_PORT'),
    },
}
