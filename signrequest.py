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

# create an instance of the API class
api_instance = signrequest_client.SignrequestsApi()
data = signrequest_client.SignRequest(
    document="YOUR_DOCUMENT_URL",
    signers=[
        {
            'email': 'signer1@example.com'
        }
    ],
    from_email="you@example.com"
)

try:
    # Send a SignRequest
    api_response = api_instance.signrequests_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->signrequests_create: %s\n" % e)