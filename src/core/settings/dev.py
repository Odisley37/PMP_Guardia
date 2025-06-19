from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]  # Permite qualquer host em desenvolvimento

# Banco de dados SQLite (para desenvolvimento)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Configurações extras para facilitar o desenvolvimento
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]  # ✅ Django Debug Toolbar (opcional)
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]
