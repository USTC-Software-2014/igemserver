"""
Django settings for IGEMServer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7jkomavmtmlifw$pbs9@wu%y^=sn37xv0on+z9@0oqp0_g7ilu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'api',
    'IGEMServer',
    'biopano',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'Middleware.TokenMiddleware',
    # 'my_auth.middleware.CookieToTokenMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

)

'''
following are:
    AUTH CONFIG------GOOGLE & LDAP
'''

AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'my_auth.TokenBackend.TokenBackend',
    'django.contrib.auth.backends.ModelBackend',
)

GOOGLE_OAUTH2_CLIENT_ID = '803598705759-nuc4bd5cm9k0ng4u91m9fa3pr05158k9.apps.googleusercontent.com'  # os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET = 'OlSa44n2HuYPfXyGPoCsXEeb'  # os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
# GOOGLE_WHITE_LISTED_DOMAINS = ['ailuropoda.org']

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'IGEMServer.urls'

WSGI_APPLICATION = 'IGEMServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'backend_master',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'master',
        'PASSWORD': 'SyntheticBiology',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


config_igemserver_local = {
    'CLIENT_ID': '646625069486-lf2c4fimrnv6eqpgt6qltv0g2vnnhuch.apps.googleusercontent.com',
    'CLIENT_SECRET': 'TFSAw1GMa_ZVY6Yr5sbLylL0',
    'REDIRECT_URL': 'http://127.0.0.1:8000/auth/oauth/google/complete/',
    'BASE_URL': r'https://accounts.google.com/o/oauth2/',
}

config_igemserver = {
    'CLIENT_ID': '774241676936-9j12b72mdoio97liq0ihps57107ja7l3.apps.googleusercontent.com',
    'CLIENT_SECRET': 'ELErpdA3rvOrN4FVdXPf5eTB',
    'REDIRECT_URL': 'http://api.biopano.org/auth/oauth/google/complete/',
    'BASE_URL': r'https://accounts.google.com/o/oauth2/',
}

config_qq = {
    'CLIENT_ID': '101152562',
    'CLIENT_SECRET': 'f9076c2757efaaeee614fc3c83997918',
    'REDIRECT_URL': 'http://feiyicheng.server.ailuropoda.org/auth/oauth/qq/complete/',
    'BASE_URL': r'https://graph.qq.com/oauth2.0/',
}

OAuthClient = {'google': config_igemserver,
               'qq': config_qq
    }