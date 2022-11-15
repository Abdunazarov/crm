from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a@wo4_vx@w1!s5f9epe)h$6mw5t&x4*ky9d2np#t^y82r6p5p4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'user.User'

# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',

    'rest_framework_swagger',



    'user',
    'apartment',
    'request_sell',
    'request_buy',
    'news',
    'others',

    'baton.autodiscover'
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'

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
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            },
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = 'static/'
STATIC_ROOT = str(BASE_DIR) + '/staticfiles/'

MEDIA_URL = 'media/'
MEDIA_ROOT = str(BASE_DIR) + '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






# BATON CONFIGURATION

BATON = {
    'SITE_HEADER': 'CRM',
    'SITE_TITLE': 'CRM',
    'INDEX_TITLE': 'CRM Администрация',
    'SUPPORT_HREF': 'https://t.me/D_Abdunazarov',
    'COPYRIGHT': 'copyright © 2022', # noqa
    'POWERED_BY': '<a href="https://t.me/D_Abdunazarov">D__Abdunazarov</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'COLLAPSABLE_USER_AREA': False,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'MENU': (

        { 'type': 'title', 'label': 'Requests', 'apps': ('request_sell', 'request_buy') },


        { 'type': 'model', 'label': 'Request for selling', 'name': 'requestsell', 'app': 'request_sell', 'icon': 'fa fa-book' }, 
        { 'type': 'model', 'label': 'Request for buying', 'name': 'requestbuy', 'app': 'request_buy', 'icon': 'fa fa-book' }, 
        


        { 'type': 'title', 'label': 'Apartments', 'apps': ('request_sell', 'request_buy') },
        { 'type': 'model', 'label': 'Apartments', 'name': 'apartment', 'app': 'apartment', 'icon': 'fa fa-building' }, 

        { 'type': 'title', 'label': 'Users', 'apps': ('request_sell', 'request_buy') },
        { 'type': 'model', 'label': 'Users', 'name': 'user', 'app': 'user', 'icon': 'fa fa-user' }, 


        { 'type': 'title', 'label': 'News', 'apps': ('request_sell', 'request_buy') },
        { 'type': 'model', 'label': 'News', 'name': 'news', 'app': 'news', 'icon': 'fa fa-newspaper' }, 


    )
}
