import os
from pathlib import Path

# Базова директорія проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Ключ безпеки (для тестового завдання підійде будь-який)
SECRET_KEY = 'django-insecure-test-key-for-erp-module'

# Увімкнений режим дебагу для розробки
DEBUG = True

ALLOWED_HOSTS = ['*']

# Наші додатки
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Сторонні бібліотеки
    'rest_framework',
    # Локальні додатки
    'orders',
]

# Проміжні шари (виправляє помилки admin.E408, E409, E410)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Шаблони (виправляє помилку admin.E403)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Налаштування PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'erp_db',
        'USER': 'erp_user',
        'PASSWORD': 'erp_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

# Виправляє попередження models.W042
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'