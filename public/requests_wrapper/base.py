#!/usr/bin/env python
#coding=utf-8
__author__ = 'messageoom'

import requests
import config
import json
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


class Request(object):
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

    def request(self, url, expected_http_code=None,expected_response_code=None, e_code=None, conf={}):
        """
        :param url:  System Request Interface
        :param expected_http_code:  The status code that the request returns
        :param expected_response_code: Returns the status code in the data after a successful request
        :param e_code:
        :param conf:
        :return:
        """
        expected_http_code = expected_http_code or self.expected_http_code
        expected_response_code = expected_response_code or self.expected_response_code
        params = conf.get('params', None)
        headers = conf.get('headers', None)
        data = conf.get('data', None)

        response = self.func(url,
                             params, headers, data)
        #if config.DEBUG:
        #    self._log_request(response.request)
        #    self._log_response(response)

        if response.status_code != expected_http_code :
            raise Exception('[Expected_http_code: %s, Response %s]: %s' % (
                str(expected_http_code), str(response.status_code), response.content))
        elif e_code is not None and e_code not in response.content:
            raise Exception('Expected: %s, Response %s' % (
                e_code, response.content))
        try:
            reCotent = response.content
            json.dumps(str(reCotent))
            responseCODE = json.loads(reCotent).get("code")
        except:
            raise Exception('[Expected_response_code: %s, Response: %s]'%(
                str(expected_response_code,responseCODE)
            ))
        else:
            if responseCODE != expected_response_code:
                raise Exception('[Expected_response_code: %s, Response: %s]'%(
                    str(expected_response_code),responseCODE
                ))
            else:
                pass

        return response

class Post(Request):
    """
    default expected_http_code=200, expected_response_code=1
    """
    expected_http_code = 200
    expected_response_code = 1

    def func(self, url, params, headers, data):
        return requests.post(url,
                            params=params, headers=headers, data=data)

#Test the encapsulated module
#Post().request("URL",conf={"data":{"loginusername":"username","loginpassword":"password"}})


class Get(Request):
    """
    default expected_http_code=200, expected_response_code=1
    """
    expected_http_code = 200
    expected_response_code = 1

    def func(self, url, params, headers, data):
        return requests.get(url,
                            params=params, headers=headers, data=data)