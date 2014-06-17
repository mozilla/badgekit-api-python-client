import hashlib
import jwt
import requests
import time
from urllib import urlencode
import urlparse

try:
  import json
except ImportError:
  import simplejson as json


class RemoteError (Exception):
    def __init__ (self, msg, code, details={}):
        Exception.__init__(self, msg)

        self.code = code
        self.details = details


errors = {
    'MethodNotAllowedError': type('MethodNotAllowedError', (RemoteError,), {}),
    'ResourceNotFoundError': type('ResourceNotFoundError', (RemoteError,), {}),
    'ValidationError': type('ValidationError', (RemoteError,), {}),
}

def make_url (endpoint, path, query=None):
    uri = urlparse.urljoin(endpoint, path);

    if query:
        parts = urlparse.urlparse(uri)._asdict()
        uriquery = urlparse.parse_qs(parts['query'])
        for key, value in query.items():
            uriquery[key] = value
        parts['query'] = urlencode(uriquery)
        parts = urlparse.ParseResult(**parts)
        uri = urlparse.urlunparse(parts)

    return uri


def make_error (body, code):
    err_name = body.get('code') or body.get('error', {}).get('code', '')
    err_msg = body.get('message') or body.get('error', {}).get('message', '')

    if err_name:
        if not err_name.endswith('Error'):
            err_name += 'Error';
    else:
        err_name = error_name_from_status_code(code)

    if err_name not in errors:
        errors[err_name] = type(str(err_name), (RemoteError,), {})

    Error = errors[err_name]
    return Error(err_msg, code, details=body.get('details'))


def error_name_from_status_code (code):
    return 'Http' + str(code) + 'Error'


class JWTAuth (requests.auth.AuthBase):
    def __init__ (self, auth):
        if (type(auth) is not dict):
            auth = {'secret': str(auth)}

        self.key = auth.get('key', 'master')
        self.secret = auth.get('secret')

    def __call__ (self, request):
        url = urlparse.urlparse(request.url)
        path = url.path
        if url.query:
            path = path + '?' + url.query

        headers = {
            'typ': 'JWT',
            'alg': 'HS256'
        }

        payload = {
            'key': self.key,
            'exp': int(time.time()) + (1000 * 60),
            'method': request.method.upper(),
            'path': path
        }

        if request.body:
            payload['body'] = {
                'alg': 'SHA256',
                'hash': hashlib.sha256(request.body).hexdigest()
            }

        signed = jwt.encode(payload, self.secret, headers=headers)

        request.headers['Authorization'] = 'JWT token="%s"' % signed

        return request


class Remote (object):

    def __init__ (self, endpoint, auth):
        self.endpoint = endpoint.rstrip('/')
        self._auth = auth

    def _request (self, request):
        return requests.request(**request)

    def _make_call (self, method, options):
        if type(options) is not dict:
            options = {'path': str(options)}

        request = {
            'url': make_url(self.endpoint, options['path'], options.get('query')),
            'method': method,
            'headers': {
                'User-Agent': 'BadgeKit API Client (Python)',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            'auth': JWTAuth(options.get('auth', self._auth))
        }

        if 'data' in options:
            # TO DO - encode file uploads
            request['data'] = json.dumps(options['data'])

        response = self._request(request)
        body = response.json()

        if response.status_code >= 400:
            raise make_error(body, response.status_code)

        generator = options.get('generator')

        if generator is not None:
            body = generator.preformat(body)

        if 'filter' in options:
            body = body.get(options['filter'])

        if 'default' in options and body is None:
            body = options['default']

        if generator is not None:
            body = generator(body)

        return body

    def get (self, options):
        return self._make_call('get', options)

    def head (self, options):
        return self._make_call('head', options)

    def post (self, options):
        return self._make_call('post', options)

    def put (self, options):
        return self._make_call('put', options)

    def delete (self, options):
        return self._make_call('delete', options)
