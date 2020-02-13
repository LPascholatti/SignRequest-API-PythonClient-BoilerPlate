from __future__ import print_function
import time
import signrequest_client
from signrequest_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
default_configuration = signrequest_client.Configuration()
default_configuration.api_key['Authorization'] = 'YOUR_TOKEN_HERE'
default_configuration.api_key_prefix['Authorization'] = 'Token'
signrequest_client.Configuration.set_default(default_configuration)