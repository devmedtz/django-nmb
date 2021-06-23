from django.shortcuts import render
from django.http import JsonResponse
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

