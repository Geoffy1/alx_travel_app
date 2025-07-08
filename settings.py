# alx_travel_app/alx_travel_app/settings.py

import os
import environ # Import django-environ

# Initialize django-environ
env = environ.Env(
    # Set casting and default values for environment variables
    DEBUG=(bool, False), # Default DEBUG to False if not specified in .env
    # Default MySQL URL: mysql://USER:PASSWORD@HOST:PORT/NAME
    DATABASE_URL=(str, 'mysql://root:@localhost:3306/alx_travel_app'),
    # Fallback secret key (for local dev if .env is missing, but should be strong)
    SECRET_KEY=(str, 'django-insecure-REPLACE_WITH_A_VERY_STRONG_SECRET_KEY'),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the directory containing settings.py's parent (which is the project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read .env file from the project root (BASE_DIR)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY') # Get SECRET_KEY from .env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') # Get DEBUG from .env

ALLOWED_HOSTS = [] # Add your domain names here in production, e.g., ['.example.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'listings', # The app you created

    # Third-party Apps
    'rest_framework',       # Django REST Framework
    'corsheaders',          # Handles Cross-Origin Resource Sharing
    'drf_yasg',             # Swagger/OpenAPI documentation
    'celery',               # For future asynchronous tasks
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Must be placed high in the list
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

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

WSGI_APPLICATION = 'alx_travel_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': env.db(), # Parse DATABASE_URL from .env file
}

# If you prefer to define database settings explicitly using individual env vars:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DB_NAME', default='alx_travel_app'),
#         'USER': env('DB_USER', default='root'),
#         'PASSWORD': env('DB_PASSWORD', default=''),
#         'HOST': env('DB_HOST', default='localhost'),
#         'PORT': env('DB_PORT', default='3306'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # For production serving

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Custom Configurations ---

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', # Adjust permissions as needed for your API
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema', # For Swagger
}

# CORS Headers settings
# For development, allowing all origins is convenient but NOT secure for production.
CORS_ALLOW_ALL_ORIGINS = True
# In production, use CORS_ALLOWED_ORIGINS to specify allowed domains:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000", # Example for your frontend
#     "https://yourfrontenddomain.com",
# ]

# Swagger/DRF-YASG settings
SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'alx_travel_app.urls.API_INFO', # Reference to API_INFO defined in urls.py
    'USE_SESSION_AUTH': False, # Set to True if you want session authentication in Swagger UI
    'DOC_EXPANSION': 'none',   # 'list' or 'full' to expand operations by default
    'DEEP_LINKING': True,      # Enable deep linking for tags and operations
    'SECURITY_DEFINITIONS': { # Example for JWT or Bearer Token authentication
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
