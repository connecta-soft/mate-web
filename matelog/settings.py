
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_3vm*3!l@^-#i92ci1me%nu5@ub9!4_s2sqo#i88ygo1aotop%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 'main', 'corsheaders',
    'django.contrib.staticfiles', 'rest_framework',
    'ckeditor_uploader', 'easy_thumbnails', 'admins'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    #'matelog.cors_midlware.CustomCorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'matelog.middleware.LoginRequiredMiddleware'
]

ROOT_URLCONF = 'matelog.urls'

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

WSGI_APPLICATION = 'matelog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'mete',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'admins/static'),

]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'product_img': {'size': (400, 400), 'crop': False},
        'ten': {'size': (120, 120), 'crop': False},
        'cart': {'size': (200, 200), 'crop': False},
        'prod_photo': {'size': (900, 900), 'crop': False},
        'btn_img': {'size': (50, 50), 'crop': False},
        'avatar': {'size': (90, 90), 'crop': False}
    },
}


LOGIN_REDIRECT_URL = '/admin/quick_applications'
LOGOUT_REDIRECT_URL = '/admin/login'



# date format
DATE_FORMAT = {'Y.m.d'}


# rest
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DATE_INPUT_FORMATS': [("%Y.%m.%d"), ("%d/%m/%Y")],
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://matelogisticss.com",
    "https://www.matelogisticss.com",
]


#CORS_ALLOW_HEADERS = (
#    'Access-Control-Allow-Headers',
#    'Access-Control-Allow-Credentials',
#    'Access-Control-Allow-Origin',
#)


CORS_ALLOW_CREDENTIALS = True
#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_HEADERS = "*"

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Language'
]

CORS_ORIGIN_WHITELIST = [
   "http://localhost:3000"
]


SRM_API_KEY = '74523oetiheutimlnutihh3948509htuiuotmjbrnthdoei84ml'



# for email
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'leads@matelogisticss.com'
EMAIL_HOST_PASSWORD = 'papzxominwbtlnzh'




# google api key
GOOGLE_API_KEY = 'AIzaSyDiWOQ9Y4Xh28n71iK_SnLmRCzrQAk638k'
