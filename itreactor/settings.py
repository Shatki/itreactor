"""
Django settings for itreactor project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p*vfv8&o&k!7zky8*-xi)$oay)v5@!1k=-!me&_%jzw1gqfvbp'

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
    'ckeditor',
    'blog',
    'web',
    'users',
    #'sorl.thumbnail',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itreactor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'itreactor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/assets/'
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Template list
TEMPLATE_HOMEPAGE = 'homepage.html'
TEMPLATE_ABOUT = 'aboutpage.html'
TEMPLATE_SERVICE = 'servicepage.html'
TEMPLATE_BLOG_LIST = 'blogpage.html'
TEMPLATE_BLOG_DETAIL = 'articlepage.html'
TEMPLATE_CONTACT = 'contactpage.html'
TEMPLATE_ELEMENTS = 'elementspage.html'

ARTICLE = u'article'

# Photos dirs list
STATIC_IMAGE_DIR = 'img/'
CONTENT_PICS_DIR = 'content/'
PROFILE_PHOTOS_DIR = 'photos/'
HEADER_PHOTOS_DIR = 'headers/'
GALLERY_PHOTOS_DIR = 'gallery/'
AWARDS_PHOTOS_DIR = 'awards/'
ARTICLE_PHOTOS_DIR = 'articles/'
DOCUMENTS_DIR = 'documents/'
DOCUMENTS_MINIATURES_DIR = 'miniatures/'

# Standard photos list
NO_PHOTO = STATIC_IMAGE_DIR + 'nophoto.png'
CONTENT_PIC_DEFAULT_NAME = CONTENT_PICS_DIR + 'image.jpg'
PROFILE_PHOTO_DEFAULT_NAME = PROFILE_PHOTOS_DIR + 'profileimage.jpg'
HEADER_PHOTO_DEFAULT_NAME = HEADER_PHOTOS_DIR + 'header.jpg'

# Application definition
AUTH_USER_MODEL = 'users.User'

# CKEDITOR Settings
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# CKEDITOR_CONFIGS по сути необязательны. Они влияют на тулбар редактора. Если выключите - будет очень мало
# инструментов для работы с текстом. После полной настройки - попробуйте с ними поиграться. Возможно найдете для себя
# какой-то более оптимальный вариант настроек!
CKEDITOR_CONFIGS = {
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
             'RemoveFormat'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'sourcearea', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Maximize', 'ShowBlocks']
        ],
    }
}

PAGINATION_ARTICLES_ON_PAGE = 3  # Количество новостей на странице
PAGINATION_LIST_RANGE = 3  # Число страниц отопбажаемых в строке пагинация между "Назад" и "Вперед"

# Memcached
# https://docs.djangoproject.com/en/3.1/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

LOGIN_REDIRECT_URL = '/'
