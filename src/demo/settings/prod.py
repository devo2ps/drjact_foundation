from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = []

#make sure password validators are running in production
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
	'default': {
		ENGINE: 'dange.db.backends.postgresql_psycopg2',
		'NAME':config('DB_NAME'), 
		'USER':config('DB_USER'),
		'PASSWORD': config('DB_PW'),
		'HOST': config('DB_HOST'),
		'PORT': ''
	}

}