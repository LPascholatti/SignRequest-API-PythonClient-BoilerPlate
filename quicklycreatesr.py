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

api_instance = signrequest_client.SignrequestQuickCreateApi()
data = signrequest_client.SignRequestQuickCreate(
    signers=[
        {
            'email':'signer1@example.com'
        }
    ],
    file_from_url='your_url',
    from_email='your@email.com'
)

try:
    # Create a Document and SignRequest
    api_response = api_instance.signrequest_quick_create_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_create: %s\n" % e)