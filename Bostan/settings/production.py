from .defaults import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
PERSISTENT_STORAGE = "/mnt/shared-volume"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PERSISTENT_STORAGE, 'db.sqlite3'),
    }
}
