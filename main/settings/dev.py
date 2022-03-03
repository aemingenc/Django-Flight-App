#base.py deki herseyi al dedik
from colorsys import TWO_THIRD
from .base import *
import os

THIRD_PART_APPS = ["debug_toolbar"]

INSTALLED_APPS += THIRD_PART_APPS

THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]