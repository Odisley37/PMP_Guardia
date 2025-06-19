## Comandos 

```bash
# 1. Criar diretório raiz
mkdir PMP_Guardia && cd PMP_Guardia

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# 3. Instalar dependências iniciais
pip install django djangorestframework pytest pytest-django

# 4. Criar estrutura de pastas
mkdir -p src apps tests docs .github/workflows
touch README.md requirements.txt
``` 
 ```bash
 cd src
django-admin startproject core .
``` 
```bash
PMP_Guardia/
│
├── .github/
│   └── workflows/       # GitHub Actions
├── docs/                # Documentação
├── src/
│   ├── apps/            # Aplicações Django (serão criadas aqui)
│   ├── core/            # Projeto Django (settings, urls, etc.)
│   └── manage.py
├── tests/               # Testes globais
├── venv/                # Ambiente virtual
├── requirements.txt     # Dependências
└── README.md
```


```bash
# 1. Criar diretório raiz
mkdir PMP_Guardia && cd PMP_Guardia

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# 3. Instalar dependências iniciais
pip install django djangorestframework pytest pytest-django

# 4. Criar estrutura de pastas
mkdir -p src apps tests docs .github/workflows
touch README.md requirements.txt
```

✅ Passo 1: Criar a pasta settings dentro de core
No terminal:
cd src/core
mkdir settings
mv settings.py settings/base.py
touch settings/dev.py settings/prod.py settings/test.py



✅ Passo 2: Atualizar core/__init__.py para tornar settings um módulo Python
Crie (ou edite) o arquivo:
touch __init__.py



✅ Passo 3: Estrutura final da pasta core após isso:
```bash
src/core/
│
├── __init__.py
├── asgi.py
├── urls.py
├── wsgi.py
└── settings/
    ├── __init__.py
    ├── base.py
    ├── dev.py
    ├── prod.py
    └── test.py
``` 

📄 base.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key")
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
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

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {}  # será sobrescrito

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


📄 dev.py

from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}



📄 prod.py

from .base import *

DEBUG = False
ALLOWED_HOSTS = ["minhaapi.com", "www.minhaapi.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}


📄 test.py

from .base import *

DEBUG = False
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test_db.sqlite3",
    }
}





[pytest]
DJANGO_SETTINGS_MODULE = core.settings.test

python src/manage.py runserver --settings=core.settings.dev

python manage.py runserver --settings=core.settings.dev


https://Odisley37.github.io/PMP_Guardia/