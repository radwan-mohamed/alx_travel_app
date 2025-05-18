import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# Add installed apps
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'listings',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

# CORS
CORS_ALLOW_ALL_ORIGINS = True  # For development only, consider restricting for production

# REST framework default settings (optional basic setup)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
