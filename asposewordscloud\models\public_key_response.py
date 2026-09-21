# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="public_key_response.py">
#   Copyright (c) 2026 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import typing_extensions
import datetime
import six
import json

class PublicKeyResponse(object):
    """REST response for RSA public key info.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'exponent': 'str',
        'modulus': 'str'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'exponent': 'Exponent',
        'modulus': 'Modulus'
    }

    def __init__(self, request_id=None, exponent=None, modulus=None):  # noqa: E501
        """PublicKeyResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._exponent = None
        self._modulus = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if exponent is not None:
            self.exponent = exponent
        if modulus is not None:
            self.modulus = modulus

    @property
    def request_id(self):
        """Gets the request_id of this PublicKeyResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this PublicKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PublicKeyResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this PublicKeyResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def exponent(self):
        """Gets the exponent of this PublicKeyResponse.  # noqa: E501

        Gets or sets RSA key exponent as Base64 string.  # noqa: E501

        :return: The exponent of this PublicKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._exponent

    @exponent.setter
    def exponent(self, exponent):
        """Sets the exponent of this PublicKeyResponse.

        Gets or sets RSA key exponent as Base64 string.  # noqa: E501

        :param exponent: The exponent of this PublicKeyResponse.  # noqa: E501
        :type: str
        """
        self._exponent = exponent

    @property
    def modulus(self):
        """Gets the modulus of this PublicKeyResponse.  # noqa: E501

        Gets or sets RSA key modulus as Base64 string.  # noqa: E501

        :return: The modulus of this PublicKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        """Sets the modulus of this PublicKeyResponse.

        Gets or sets RSA key modulus as Base64 string.  # noqa: E501

        :param modulus: The modulus of this PublicKeyResponse.  # noqa: E501
        :type: str
        """
        self._modulus = modulus


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other