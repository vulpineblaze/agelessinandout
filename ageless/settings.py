"""
Django settings for ageless project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pp657r8jxh#=i)^pov0w!oi!!bj$jtrpc5((c*_pb(x9x5yd*d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    ###

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [] 
# ALLOWED_HOSTS = ['.yourcompusolutions.com',
#                 '.yourcompusolutions.com',
#                 '.agelessinandout.com',
#                 '.agelessinandout.com',
#                 '.localhost.',
#                 'locahost']

SITE_ID = 1

# Application definition #

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'inandout',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ageless.urls'

WSGI_APPLICATION = 'ageless.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/ ####

STATIC_URL = '/static/'

STATIC_ROOT = "/webapps/ageless/livestatic/"

# List of finder classes that know how to find static files in
# various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )


STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
    # '/webapps/hello_django/personal_tracker/core/static/',
    '/webapps/ageless/static/',
]


# TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = ( 'django.contrib.auth.context_processors.auth',
                                'django.core.context_processors.request', )

TEMPLATE_LOADERS = (

    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/webapps/ageless/inandout/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

MEDIA_ROOT = '/webapps/ageless/media'
MEDIA_URL = '/media/'




# STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATIC_JS_DIR = os.path.join(STATIC_DIR, "js")
# TINYMCE_JS_ROOT = os.path.join(STATIC_JS_DIR, "tiny_mce")
# TINYMCE_JS_URL = os.path.join(TINYMCE_JS_ROOT, "tiny_mce.js")

# TINYMCE_JS_ROOT=STATIC_ROOT+"static/tiny_mce"
# TINYMCE_JS_URL=TINYMCE_JS_ROOT+"tiny_mce.js"


# TINYMCE_JS_ROOT = '/media/tiny_mce/'
# TINYMCE_JS_URL = os.path.join(MEDIA_URL, "tiny_mce/tiny_mce_src.js")

# TINYMCE_JS_URL = STATIC_URL+'inandout/js/tinymce/tinymce.min.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,preview",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,

    'file_browser_callback': 'mce_filebrowser',

    'height': "640",
    'width': "80%",
    'theme_advanced_buttons3_add' : "preview",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = False




