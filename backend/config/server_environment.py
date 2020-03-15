import os

# Environment variables

# Mongo hostname
MONGO_HOSTNAME = os.environ.get('MONGO_HOSTNAME', 'localhost')

# Mongo port
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)

# IPManager base collection
TESTING_COLLECTION = os.environ.get('TESTING_COLLECTION', 'ipm_root_testing')
BASE_COLLECTION = os.environ.get('BASE_COLLECTION', TESTING_COLLECTION)

# Password encryption key (testing)
ENC_KEY = os.environ.get(
    'ENC_KEY', 'KM1tL17icOwO7QkzOy4wrTVUSUfr10CEFIFDvAZpI40=').encode()

# JWT encryption key (testing)
JWT_ENC_KEY = os.environ.get(
    'JWT_ENC_KEY', 'G-yEgpe9MNBzRC14UQ_3lHtNkiY6z2enG1KzY33Vcvw=')

DOCKER_BASE_URL = os.environ.get(
    'DOCKER_BASE_URL', 'unix://var/run/docker.sock')

ANSIBLE_PATH = os.environ.get('ANSIBLE_PATH', './')
