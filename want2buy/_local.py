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

LIQPAY_PUBLIC_KEY = ''
LIQPAY_PRIVATE_KEY = ''
DOMAIN_NAME = 'w2b.webmonstr.com'