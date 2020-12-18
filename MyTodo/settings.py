"""
Django settings for MyTodo project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
from decouple import config
from decouple import Csv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn= config("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '8zp9)ms5@@-m02o%stblzs7=(4blcsptn-$2+zrwcwn8t6=ur8'
SECRET_KEY = config('SECRET_KEY')

ENVIRONMENT = config('ENVIRONMENT', default='production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

#ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #debug_toolbar
    'debug_toolbar',

    #django allauth
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount',
    

    #django allauth provider
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook', 

    #local app
    'todoapp',
    'contact',

    #third party
    'crispy_forms',
    'sri',
]

#debug_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#whitenoise
    # 'django.middleware.cache.UpdateCacheMiddleware', #cache 
    'django.middleware.common.CommonMiddleware', 
    # 'django.middleware.cache.FetchFromCacheMiddleware',#cache 
    # 'csp.middleware.CSPMiddleware',#django-csp
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',#debug_toolbar
    "django.middleware.common.BrokenLinkEmailsMiddleware", #Manager
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    

]

ROOT_URLCONF = 'MyTodo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyTodo.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', 
)

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    #'default': {
    #    'ENGINE': config('DB_ENGINE'),
    #    'NAME': config('DB_NAME'),
    #    'USER': config('DB_USER'),
    #    'PASSWORD': config('DB_PASSWORD'),
    #    'HOST': config('DB_HOST'),
    #    'PORT': config('DB_PORT', cast=int),
    #}
}

DATABASE_URL = config('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500)
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


#static config
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = 'todoapp:home'
ACCOUNT_LOGOUT_REDIRECT = 'todoapp:home' 

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =  config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS  =  config('EMAIL_USE_TLS', cast=bool)

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
print(DEFAULT_FROM_EMAIL)

SERVER_EMAIL = DEFAULT_FROM_EMAIL

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =  True 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True 
ACCOUNT_USERNAME_REQUIRED  = True
ACCOUNT_UNIQUE_USERNAME = True 


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


MANAGER = (
    ('Jokotoye Ademola', 'jokotoyeademola95@gmail.com')
)

ADMIN = (
    ('Jokotoye Ademola', 'jokotoyeademola95@gmail.com')
)

if ENVIRONMENT == 'production':
    #SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    CACHE = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', 
            'LOCATION': '127.0.0.1:11211',
            'OPTIONS': {
                'server_max_value_length': 1024 * 1024 * 2,
            }

        }
    }
    
    #HTTP Strict Transport Security (HSTS)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_PRELOAD = True

    #Cross-Site Request Forgery (CSRF)
    CSRF_COOKIE_SECURE = True  # cookie will only be sent over an HTTPS connection
    CSRF_COOKIE_HTTPONLY = True  # only accessible through http(s) request, JS not allowed to access csrf cookies

    
    X_FRAME_OPTIONS = 'DENY'
    #SECURE_REFERRER_POLICY = 'same-origin'
    
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    #Cross-Site Scripting (XSS)
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_HTTPONLY = True
    #django-csp(Details at official docs)

django_heroku.settings(locals())