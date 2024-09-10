import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOCS_ACCESS = "staff"

ENVIRONMENT = "development"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-e^w6_hl!28up3rk2p)jl#=yvy&q_a0xsn8c=j@-4-=-^mw0+5="

# INSTALLED_APPS += [
#     "debug_toolbar",
# ]

# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "glancefy_db"),
        "USER": os.environ.get("DB_USER", "glancefy_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "glancefy_password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

CELERY_BEAT_SCHEDULE = {
    "scrape-articles-every-15s": {
        "task": "article_collection.tasks.scrape_articles",
        "schedule": 15.0,
    },
}


message = f"{ENVIRONMENT} settings loaded".upper()
print(f"{message:-^50}")
