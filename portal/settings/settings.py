"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q@fcesjgk=6x1awz=63b8aczx3#qb7rp_o3^$-^f@7)2wwr#@)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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

ROOT_URLCONF = "portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "portal.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
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

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/public/portal/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
INSTALLED_APPS += ["main.apps.MainConfig", "django_tables2", "django_filters"]
TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "main.context_processors.app_name",
    "main.context_processors.app_version",
    "main.context_processors.external_links",
]
TEMPLATES[0]["DIRS"] = list(
    (BASE_DIR / "main" / "repositories" / "plugins").glob("*/templates")
)
APP_NAME = "CHAMP"

DATABASES["default"]["NAME"] = BASE_DIR / "db" / "db.sqlite3"


CONTACT_EMAIL = "c.cave-ayland@imperial.ac.uk"
DEFAULT_FROM_EMAIL = "noreply@imperial.ac.uk"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_ROOT = "/var/www/ood/public/portal/"
LOGIN_URL = "main:login"
LOGOUT_REDIRECT_URL = "main:index"

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(name)-8s  %(levelname)-8s %(asctime)s.%(msecs)03d  :    %(message)s"  # noqa: E501
        }
    },
    "handlers": {
        "console": {
            "level": LOGGING_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": LOGGING_LEVEL,
            "class": "logging.FileHandler",
            "filename": os.getenv("LOGGING_FILE", "/tmp/portal.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {APP_NAME: {"handlers": ["console", "file"], "level": LOGGING_LEVEL}},
}

JOBS_DIR = Path(os.getenv("JOBS_DIR", str(BASE_DIR / "portal_jobs")))


PORTAL_CONFIG_PATH = os.getenv("PORTAL_CONFIG_PATH", "portal_config.yaml")

VERSION = "2.0.0"
