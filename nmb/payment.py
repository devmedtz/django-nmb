import json
from enum import Enum
import requests
from requests.auth import HTTPBasicAuth


class APIRequest:

    def __init__(self, context=None):
        self.context = context

    def execute(self):
        if self.context is not None:
            try:
                return {
                    APIMethodType.POST: self.__post
                }.get(self.context.method_type, self.__unknown)()
            except requests.exceptions.ConnectionError as ce:
                print(ce)
                return None
        else:
            raise TypeError('Context cannot be None.')

    def __post(self):
        r = requests.post(self.context.address, auth=HTTPBasicAuth(self.context.api_username,self.context.api_password), json=self.context.parameters)
        print(r)
        return APIResponse(json.loads(r.headers.__str__().replace("'", '"')), json.loads(r.text))

    def __unknown(self):
        raise Exception('Unknown Method')


class APIResponse(dict):

    def __init__(self, headers, body):
        super(APIResponse, self).__init__()
        self['headers']: dict = headers
        self['body']: dict = body

    @property
    def headers(self) -> dict:
        return self['headers']

    @headers.setter
    def headers(self, headers: dict):
        if type(headers) is not dict:
            raise TypeError('Headers must be a dict')
        else:
            self['headers'] = headers

    @property
    def body(self) -> dict:
        return self['body']

    @body.setter
    def body(self, body: dict):
        if type(body) is not dict:
            raise TypeError('Body must be a dict')
        else:
            self['body'] = body


class APIMethodType(Enum):
    GET: int = 0
    POST: int = 1


class APIContext(dict):

    def __init__(self, api_password='', api_username='', method_type=APIMethodType.GET, address='', parameters={}):
        super(APIContext, self).__init__()

        self['api_password']: str = api_password
        self['api_username']: str = api_username
        self['method_type']: Enum = method_type
        self['address']: str = address
        self['parameters']: dict = parameters


    @property
    def api_password(self) -> str:
        return self['api_password']

    @api_password.setter
    def api_password(self, api_password: str):
        if type(api_password) is not str:
            raise TypeError('API password must be a str')
        else:
            self['api_password'] = api_password

    @property
    def api_username(self) -> str:
        return self['api_username']

    @api_username.setter
    def api_username(self, api_username: str):
        if type(api_username) is not str:
            raise TypeError('API username must be a str')
        else:
            self['api_username'] = api_username

    @property
    def method_type(self) -> APIMethodType:
        return self['method_type']

    @method_type.setter
    def method_type(self, method_type: APIMethodType):
        if type(method_type) is not APIMethodType:
            raise TypeError('method_type must be a POST/GET')
        else:
            self['method_type'] = method_type

    @property
    def address(self) -> str:
        return self['address']

    @address.setter
    def address(self, address: str):
        if type(address) is not str:
            raise TypeError('Address must be a str')
        else:
            self['address'] = address
            