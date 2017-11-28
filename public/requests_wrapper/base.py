__author__ = 'messageoom'

import config
import requests
from urlparse import urlparse

REQUEST_FORMATTER = """
{method} {path} HTTP/1.1
HOST: {host}
{headers}

{body}
"""
RESPONSE_FORMATTER = """
HTTP/1.1 {status}
{headers}

{body}
"""

class  MeRequest(object):
    def _log_request(self, request):
        print REQUEST_FORMATTER.format(
            method=request.method,
            path=request.path_url,
            host=urlparse(request.url).netloc,
            headers='\n'.join(
                ["%s: %s" % (k, v) for k, v in request.headers.iteritems()]
            ),
            body=request.body
        )

    def _log_response(self, response):
        print RESPONSE_FORMATTER.format(
            status=str(response.status_code),
            headers='\n'.join(
                ["%s: %s" % (k, v) for k, v in response.headers.iteritems()]
            ),
            body=response.content
        )

    def request(self, path, expected=None, e_code=None, conf={}):
        expected = expected or self.expected
        params = conf.get('params', None)
        headers = conf.get('headers', None)
        data = conf.get('data', None)
        #cookies = conf.get('cookies',None)

        if '?' in path and params is not None:
            # Special treatment
            path += '&' + '&'.join(
                ['%s=%s' % (k, v) for k, v in params.iteritems()])
            params = None

        response = self.func(self.auth.base_url+path, self.auth.auth,
                             params, headers, data)
        if config.DEBUG:
            self._log_request(response.request)
            self._log_response(response)

        if response.status_code != expected:
            raise Exception('[Expected: %s, Response %s]: %s' % (
                str(expected), str(response.status_code), response.content))
        elif e_code is not None and e_code not in response.content:
            raise Exception('Expected: %s, Response %s' % (
                e_code, response.content))

        return response


class Post(MeRequest):
    expected = 1

    def func(self, url, auth, params, headers, data):
        return requests.post(url, data, None, auth=auth,
                             params=params, headers=headers)


class Get(MeRequest):
    expected = 1

    def func(self, url, auth, params, headers, data):
        return requests.get(url, cookies=cookies,
                            params=params, headers=headers, data=data)