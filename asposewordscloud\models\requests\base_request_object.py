import json
import os
import re
import datetime
import tempfile
import uuid

import six
from requests_toolbelt.multipart import decoder
import asposewordscloud.models
from asposewordscloud.api_client import rest


class BaseRequestObject(object):
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # pylint: disable=undefined-variable
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def getparts(self, response):
        return decoder.MultipartDecoder(response.data, response.getheader('Content-Type'), 'UTF-8').parts

    def get_original_request(self):
        return self
