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
