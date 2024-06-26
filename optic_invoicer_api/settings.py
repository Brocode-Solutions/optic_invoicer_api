import os
import environ
from pathlib import Path
import dj_database_url
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='your-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = [
    '*',
    'optic-invoicer-ui.vercel.app',
    'optic-invoicer-ui-v2-aneeshni47.vercel.app',
    'optic-invoicer-ui-v2.vercel.app',
    'optic-invoicer-api-fbd12c65eacc.herokuapp.com',
    'opticinvoicer.brocodesolutions.com'
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'https://optic-invoicer-ui.vercel.app',
    'https://optic-invoicer-ui-v2-aneeshni47.vercel.app',
    'https://optic-invoicer-ui-v2.vercel.app',
    'https://optic-invoicer-api-fbd12c65eacc.herokuapp.com',
    'https://opticinvoicer.brocodesolutions.com'
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://optic-invoicer-ui.vercel.app',
    'https://optic-invoicer-ui-v2-aneeshni47.vercel.app',
    'https://optic-invoicer-ui-v2.vercel.app',
    'https://optic-invoicer-api-fbd12c65eacc.herokuapp.com',
    'https://opticinvoicer.brocodesolutions.com'
]

CORS_ALLOW_CREDENTIALS = True

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './optic_invoicer_api/logs/logfile.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },

        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'optic_invoicer_api': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        },
    },
}


# Application definition

INSTALLED_APPS = [
    'accounts',
    'knox',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    "corsheaders",
    'organizations',
    'customers',
    'inventory',
    'invoices',
    'staff',
    'wholesale',
    'rest_framework_swagger',
    'rest_framework',
    'drf_yasg',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'optic_invoicer_api.custom_cursor_pagination.CustomCursorPagination',
    'PAGE_SIZE': 10,  # Default page size
    'EXCEPTION_HANDLER': 'optic_invoicer_api.custom_exception_handler.custom_exception_handler'

}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'optic_invoicer_api.custom_db_connection_manager.CloseOldConnectionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'optic_invoicer_api.organization_middleware.OrganizationMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

FRONTEND_URL = 'https://opticinvoicer.brocodesolutions.com/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FROM_EMAIL = env('EMAIL_FROM_EMAIL')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')

ROOT_URLCONF = 'optic_invoicer_api.urls'

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

WSGI_APPLICATION = 'optic_invoicer_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if os.environ.get('DATABASE_URL'):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if 'sslmode=require' not in DATABASE_URL:
        DATABASE_URL = f"{DATABASE_URL}?sslmode=require"
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=60, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', default="ap-south-1")

# CELERY_BROKER_URL = env('STACKHERO_RABBITMQ_AMQP_URL_TLS', None)
# Tell Django to use S3 for file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ensure HTTPS in pagination links in production
if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

    # Ensure HTTPS in pagination links
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    USE_X_FORWARDED_HOST = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
else:
    CORS_ALLOW_ALL_ORIGINS = True
