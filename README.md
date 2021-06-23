# django-nmb

A Django application which assist on integration of your web application with NMB BANK Merchant payment gateway with easy step. [docs](https://test-nmbbank.mtf.gateway.mastercard.com/api/documentation/integrationGuidelines/index.html?locale=en_US)

## Prerequisites

* Python 3.6+
* Pip or Pipenv

## It will Cover

* [x] Generate sessionID to initiate payment
* [x] Cover Hosted Checkout and Hosted Session on "example" module found on github [here](https://github.com/devmed/django-nmb)
* [ ] Direct payment
* [ ] Batch payment

## Installation

This package is available in [Python Package Index](https://pypi.org/project/django-nmb/) and can be installed using `pip` or `pipenv`

1. Run ``pip install django-nmb``
2. Add ``nmb`` to ``INSTALLED_APPS``
3. Run ``pip install requests``

## Usage

### Register account on NMB Ecommerce merchant by visit on NMB Branch near you and your will get the following credentials for testing

1. MERCHANT ID
2. MERCHANT API PASSWORD

## Open "settings.py" on your project, set the following variables

1. MERCHANT_ID = "your merchant id"
2. API_USERNAME = "merchant.merchant_id"
3. API_PASSWORD = "your api password"
4. API_ADDRESS = "https://test-nmbbank.mtf.gateway.mastercard.com/api/rest/version/60/merchant/{merchant_id}/session"

## After setting above,Then on your views.py file.

```python
from django.conf import settings
from nmb.payment import APIContext, APIMethodType, APIRequest

def get_sessionID(request):

	merchant_id = settings.MERCHANT_ID
	api_password = settings.API_PASSWORD
	api_username = settings.API_USERNAME
	address = settings.API_ADDRESS

	# Create Context with API to request a Session ID
	api_context = APIContext()

	# API USERNAME
	api_context.api_username = api_username

	# API Password
	api_context.api_password = api_password

	# API address
	api_context.address = address

	# Method type (can be GET/POST)
	api_context.method_type = APIMethodType.POST

	# Define your purchaces parameters
	parameters = {
		'apiOperation': 'CREATE_CHECKOUT_SESSION',
		'interaction': {
			'operation':'PURCHASE',
		},
		'order': {
			'id': "2",
			'amount': 100.0,
			'currency': 'TZS',
			'reference': '99676542',
			'description': 'A pair of shoes'
		}
	}

	# add parameters on request session
	api_context.parameters = parameters

	#Do the API call and put result in a response packet
	api_request = APIRequest(api_context)

	result = None

	try:
		result = api_request.execute()
	except Exception as e:
		print('Call Failed:', e)

	if result is None:
		raise Exception('Call failed to get result. Please check.')

	print(result.headers)
	print(result.body)
	
	return JsonResponse(data=result.body, safe=False)
```

### sample response

```python
{"merchant": "993755100084", "result": "SUCCESS", "session": {"id": "SESSION0002323910607J44443070E2", "updateStatus": "SUCCESS", "version": "f7f4198201"}, "successIndicator": "6d7323cd979444f2"}
```

### For full example on how to integrate please visit the github repo on example folder you will find all source codes [here](https://github.com/devmed/django-nmb)

## Give it a star

If you found this repository useful, give it a star so as the whole community of Tanzania developers can get to know it.

## Bug bounty?

If you encounter issue with the usage of the package, feel free raise an issue so as we can fix it as soon as possible(ASAP).

## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible
