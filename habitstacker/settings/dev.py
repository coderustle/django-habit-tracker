import os
from .base import *  # noqa: F403


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "database/dev.sqlite3",  # noqa: F405
    }
}
