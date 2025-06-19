from .base import *

DEBUG = True
SECRET_KEY = "testing"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
