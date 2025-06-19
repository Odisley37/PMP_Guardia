from .base import *

DEBUG = False
ALLOWED_HOSTS = (
    os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else []
)

# Banco de dados PostgreSQL (para produção)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

# Segurança adicional em produção
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True

# Verificação para evitar configuração incorreta
if DEBUG:
    raise ValueError("❌ DEBUG deve ser False em produção!")

if not ALLOWED_HOSTS:
    raise ValueError("❌ ALLOWED_HOSTS deve ser configurado em produção!")
