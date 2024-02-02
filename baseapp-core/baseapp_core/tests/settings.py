"""
Django settings for newproject project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from collections import OrderedDict
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from baseapp_core.settings.env import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APPS_DIR = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "secret-for-test-app"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "djmail",
    "baseapp_core",
    "easy_thumbnails",
    "constance",
    "constance.backends.database",
    "pgtrigger",
    "pghistory",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "baseapp_core.urls"

# Sites
URL = env("URL", "", required=False)
FRONT_URL = env("FRONT_URL", "", required=False)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".j2",
            "constants": {"URL": URL, "FRONT_URL": FRONT_URL},
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "baseapp_core.asgi.application"
WSGI_APPLICATION = "baseapp_core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
        "HOST": env("DB_SERVICE"),
        "PORT": env("DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [("en", _("English"))]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

THUMBNAIL_CACHE = "default"

CELERY_BEAT_SCHEDULE = {}

# Email
DEFAULT_FROM_EMAIL = "john@test.com"
DJMAIL_REAL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Channels
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

# GraphQL
GRAPHENE = {
    "SCHEMA": "testproject.graphql.schema.schema",
    "MIDDLEWARE": (
        "baseapp_core.graphql.LogExceptionMiddleware",
        "baseapp_core.graphql.TokenAuthentication",
    ),
    "SCHEMA_OUTPUT": "schema.graphql",
}

# Must be absolute URLs for use in emails.
MEDIA_ROOT = str(BASE_DIR.parent / "media")
MEDIA_URL = "{url}/media/".format(url=URL)

STATIC_ROOT = str(BASE_DIR.parent / "static")
STATIC_URL = "{url}/static/".format(url=URL)

# Constance
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = OrderedDict(
    [
        (
            "USER_PASSWORD_EXPIRATION_INTERVAL",
            (
                365 * 2,
                "The time interval (in days) after which a user will need to reset their password.",
            ),
        ),
    ]
)

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "baseapp_core.rest_framework.pagination.DefaultPageNumberPagination",
    "PAGE_SIZE": 30,
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "ORDERING_PARAM": "order_by",
    "SEARCH_PARAM": "q",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}
