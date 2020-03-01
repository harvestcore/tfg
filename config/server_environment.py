import os

# Environment variables

# Server environment
# Possible values:
#   'P' = production
#   'D' = development
ENVIRONMENT = 'D'

# Mongo hostname
MONGO_HOSTNAME = 'localhost' if ENVIRONMENT == 'P' else '172.17.0.2'
# Mongo port
MONGO_PORT = 27017

# IPManager base collection
BASE_COLLECTION = 'ipm_root' if ENVIRONMENT == 'P' else 'ipm_root_testing'

# Password encryption key (testing)
ENC_KEY = 'KM1tL17icOwO7QkzOy4wrTVUSUfr10CEFIFDvAZpI40='.encode() \
    if os.environ.get('ENC_KEY', None) is None else os.environ.get('ENC_KEY')

# JWT encryption key (testing)
JWT_ENC_KEY = 'G-yEgpe9MNBzRC14UQ_3lHtNkiY6z2enG1KzY33Vcvw=' \
    if os.environ.get('JWT_ENC_KEY', None) is None \
    else os.environ.get('JWT_ENC_KEY')

DOCKER_BASE_URL = 'unix://var/run/docker.sock'

ANSIBLE_PATH = './'
