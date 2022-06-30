# Get to Google Analytics API


### Importing packages

# pip install --upgrade google-api-python-client
# pip install oauth2client
# pip install google-auth-oauthlib
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

### Setup API Connection
# 1. Scope - will be requesting read-only access to the API
# 2. location of JSON key file
# 3. View ID from Universal Analytics

# SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
# KEY_FILE_LOCATION = '.env'
# VIEW_ID = '269717559'
#
# ### Connecting to the API
#
# credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)




















#
