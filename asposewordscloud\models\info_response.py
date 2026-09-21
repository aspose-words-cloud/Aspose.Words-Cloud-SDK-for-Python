# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="info_response.py">
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

class InfoResponse(object):
    """Response with API info.
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
        'additional_info': 'list[InfoAdditionalItem]',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'additional_info': 'AdditionalInfo',
        'name': 'Name',
        'version': 'Version'
    }

    def __init__(self, request_id=None, additional_info=None, name=None, version=None):  # noqa: E501
        """InfoResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._additional_info = None
        self._name = None
        self._version = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if additional_info is not None:
            self.additional_info = additional_info
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def request_id(self):
        """Gets the request_id of this InfoResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this InfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InfoResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this InfoResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def additional_info(self):
        """Gets the additional_info of this InfoResponse.  # noqa: E501

        Gets or sets AdditionalInfo.  # noqa: E501

        :return: The additional_info of this InfoResponse.  # noqa: E501
        :rtype: list[InfoAdditionalItem]
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this InfoResponse.

        Gets or sets AdditionalInfo.  # noqa: E501

        :param additional_info: The additional_info of this InfoResponse.  # noqa: E501
        :type: list[InfoAdditionalItem]
        """
        self._additional_info = additional_info

    @property
    def name(self):
        """Gets the name of this InfoResponse.  # noqa: E501

        Gets or sets Name.  # noqa: E501

        :return: The name of this InfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfoResponse.

        Gets or sets Name.  # noqa: E501

        :param name: The name of this InfoResponse.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this InfoResponse.  # noqa: E501

        Gets or sets Version.  # noqa: E501

        :return: The version of this InfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InfoResponse.

        Gets or sets Version.  # noqa: E501

        :param version: The version of this InfoResponse.  # noqa: E501
        :type: str
        """
        self._version = version


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._additional_info is not None:
            for elementAdditionalInfo in self._additional_info:
                if elementAdditionalInfo is not None:
                    elementAdditionalInfo.validate()




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
        if not isinstance(other, InfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other