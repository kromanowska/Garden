import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'vpr-&htp7-ao$4=8nwjz&ikg55-%=tw*y31^beo5-i-g$^ps_d'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django_cleanup',
    'phonenumber_field',
    'common',
    'users',
    'departments',
    'evaluations'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'garden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'garden.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

DATE_FORMAT = 'Y-m-d'
SHORT_DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'

# Static

STATIC_URL = '/static/'

# Media

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/files/'

# Source: https://github.com/johnsensible/django-sendfile
SENDFILE_ROOT = MEDIA_ROOT
SENDFILE_URL = '/media/'
SENDFILE_BACKEND = 'sendfile.backends.development'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[GARDEN] '
EMAIL_HOST_USER = ''  # TODO
EMAIL_HOST_PASSWORD = ''  # TODO
DEFAULT_FROM_EMAIL = ''  # TODO
EMAIL_USE_TLS = True
