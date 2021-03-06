import os

JWT_SECRET = 'd3f73888-f725-41f2-ae33-df5bbaf99cbc'

SECRET_KEY = "8e06922f-b52e-4203-ba61-66d54594e49e"

HOST_IP = os.environ.get('BACKEND_IP', '0.0.0.0')
HOST_PORT = os.environ.get('BACKEND_PORT', '8000')

DEBUG = os.environ.get('DEBUG', 'True')

MONGO_COLLECTION_LOGGER = 'logger'

LOGGER_SETTINGS = {
    'version': 1,
    'formatters': {
        'default': {
             'format': '%(asctime)s %(levelname)s - %(message)s',
         }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'level': 'DEBUG',
         },
    },
    'loggers': {
        'statistics': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
}

# Options: JWT, SESSION
AUTHORIZATION_METHOD = 'JWT'

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

connection = 'postgresql://{0}:{1}@{2}/{3}'.format(
    os.environ.get('DATABASE_USER'),
    os.environ.get('DATABASE_PASSWORD'),
    os.environ.get('DATABASE_HOST'),
    os.environ.get('DATABASE_DB'),
)

test_connection = 'postgresql://{0}:{1}@{2}/{3}'.format(
    os.environ.get('DATABASE_USER'),
    os.environ.get('DATABASE_PASSWORD'),
    os.environ.get('DATABASE_TEST_HOST'),
    os.environ.get('DATABASE_TEST_DB'),
)

try:
    from local_settings import *
except ImportError:
    pass
