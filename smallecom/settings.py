"""
Django settings for smallecom project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from rest_framework.permissions import AllowAny
from corsheaders.defaults import default_headers


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c7!5t*wki)lv=r7lbsrlgy(pqb2gbr01!1k5&x+wjhjm$fv57c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecom_app',
    'rest_framework',
    'corsheaders',
    
]
#


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
]
REST_FRAMEWORK = {
        
                 }


'''DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.AllowAny'],
                  'DEFAULT_AUTHENTICATION_CLASSES': 
        ['rest_framework.authentication.TokenAuthentication'], '''

'''DEFAULT_PERMISSION_CLASSES':['rest_framework.persmissions.IsAuthenticated'],
'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication']'''


'''DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),'''



CORS_ALLOWED_ORIGINS=[
    #'http://localhost:3000',
    #"http://192.168.1.14:8081"
    "http://localhost:19006"
]

CORS_ALLOW_HEADERS=[
    'accept',
    'Content-Type',
]
CORS_ALLOW_METHODS=[
    'GET',
    'POST',
    'PUT',
    'OPTIONS'
]
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'smallecom.urls'
CORS_ALLOW_HEADERS = list(default_headers) + [
    'Authorization',
]

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

WSGI_APPLICATION = 'smallecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES ={
        'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME':'ecomerces',
            'USER':'root',
            'PASSWORD':'hari123.0',
            'HOST':'127.0.0.1',
            'PORT':'3306'
        },
       
         
    }




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
#AUTH_USER_MODEL='ecom_app.CustomUser'
FILE_UPLOAD_HANDLERS=[
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'
STATICFILES_DIR=[BASE_DIR/'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage'
FILE_UPLOAD_MAX_MEMORY_SIZE=5242880


# Default session engine
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Cookie settings
SESSION_COOKIE_NAME = 'sessionid'
'''SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 1209600  # Two weeks, in seconds
SESSION_SAVE_EVERY_REQUEST = True'''
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}