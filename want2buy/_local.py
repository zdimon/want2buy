import os
from .settings import BASE_DIR
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'w2b',
        'USER': 'postgres',
        'PASSWORD': '1q2w3e',
        'HOST': 'localhost',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
