import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Mongodb settings
MONGODB_SETTINGS_DB = os.getenv('MONGODB_SETTINGS_DB', 'admin')
MONGODB_SETTINGS_USERNAME = os.getenv('MONGODB_SETTINGS_USERNAME', 'admin')
MONGODB_SETTINGS_PASSWORD = os.getenv('MONGODB_SETTINGS_PASSWORD', 'password')
MONGODB_SETTINGS_HOST = os.getenv('MONGODB_SETTINGS_HOST', 'localhost')
MONGODB_SETTINGS_PORT = int(os.getenv('MONGODB_SETTINGS_PORT', '27017'))

PORT = os.getenv('PORT', '5000')

# default PerPage parameter for GET /data
PER_PAGE = 20