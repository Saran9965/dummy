from pathlib import Path
import dj_database_url  
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aeb3w3m^-#o1)qb45ypkg$r5zgm$nz!63okw#-95$4=)pywowj'
# Ensure sessions are saved in the database
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Add this if behind a proxy/load balancer (like Render)
# Recognize secure connections behind Render's proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Enable secure cookies if using HTTPS
# If using HTTPS on Render
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# Allow your deployed domain
CSRF_TRUSTED_ORIGINS = ['https://vconnect-home-services.onrender.com']

# Optional, if needed for frontend/backend split
CORS_ALLOW_ALL_ORIGINS = True  # Or restrict to your frontend domain

DEBUG = False  #default is True i can change that it is False because of hosting

# if u can false the debug is can't allowed static files

ALLOWED_HOSTS = ['*']

import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://vconnect_user:f2qehAKwRNeVsOXnFfFpDtv2Lis6ExcC@dpg-d04ulfmuk2gs73e2lbd0-a.singapore-postgres.render.com/vconnect',
        conn_max_age=600,
        ssl_require=True  # Important for Render
   )
}
DATABASES['default']=dj_database_url.parse("postgresql://vconnect_user:f2qehAKwRNeVsOXnFfFpDtv2Lis6ExcC@dpg-d04ulfmuk2gs73e2lbd0-a.singapore-postgres.render.com/vconnect")

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
STATICFILES_DIRS = [BASE_DIR / "static"]
# Directory where collectstatic will copy your static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # python manage.py collectstatic

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'  # This ensures Django redirects to your actual login page
LOGIN_REDIRECT_URL = '/home/'  # Redirect after successful login
LOGOUT_REDIRECT_URL = '/login/'  # Redirect after logout
