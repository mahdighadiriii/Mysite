"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%=s%n1k(0qwyf52x30tjf&nt656l+a!awy$n7al2fmm2igi62q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',


    'django_summernote',
    'django.contrib.humanize',
    'django_extensions',
    
    'django.contrib.sitemaps',
    'robots',
    'debug_toolbar',
    'taggit',
    'django_recaptcha',
    'captcha',
    'crispy_forms',
    "crispy_bootstrap5",
    'website',
    'blog',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# sites framework
SITE_ID = 2

# robots
ROBOTS_USE_HOST = True
ROBOTS_USE_SITEMAP = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]


#summer note

SUMMERNOTE_THEME = 'bs4'

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,


    

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Toolbar customization
        
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    }
}




#recaptcha

RECAPTCHA_PUBLIC_KEY = '6LccbDMpAAAAAE2Lb0u1P3r5h-M_bk-tegrCPLhB'
RECAPTCHA_PRIVATE_KEY = '6LccbDMpAAAAAGylqUbYTSisikE4Upjyzf8_tPCU'
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

#captcha admin settings

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {

        'APP': {
            'client_id': '24700e10eb0c3f228a9b',
            'secret': 'fa6492387f61bcb8ddb74420d275766100c19ff9',
            'key': ''
        }

    }
}

