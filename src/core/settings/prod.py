from .base import *

DEBUG = False
ALLOWED_HOSTS = ["minhaapi.com", "www.minhaapi.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "pmpdb"),
        "USER": os.getenv("DB_USER", "pmpuser"),
        "PASSWORD": os.getenv("DB_PASSWORD", "pmppass"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}
