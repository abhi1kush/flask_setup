from .common import *

HOST_URL = '127.0.0.1'
HOST_PORT = 5005
DEBUG = True
TESTING = False
SENTRY_DSN = ""

# Elastic Search
ES_CLUSTER_CONFIG = [
    {
        "host": "127.0.0.1",
        "port": 9200
    }
]