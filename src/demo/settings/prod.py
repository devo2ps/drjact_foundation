from .base import *

DEBUG = False
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
		'NAME':'generico',
		'USER':'gen_admin',
		'PASSWORD': 'idk?',
		'HOST': 'localhost',
		'PORT': ''
	}

}