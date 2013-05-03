import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{ project_name }}',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '{{ project_name }}',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

#COMPRESS_PRECOMPILERS = (
#    ('text/less', '/home/{{ project_name }}/node_modules/.bin/lessc {infile} {outfile}'),
#)

STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', '..', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', '..', '..', '..', 'media')

FACEBOOK_APP_ID='App ID here'
FACEBOOK_API_SECRET='App Secret here'
