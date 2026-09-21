# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="stat_data_response.py">
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

class StatDataResponse(object):
    """The REST response with document's statistical data.
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
        'document_link': 'FileLink',
        'stat_data': 'DocumentStatData'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'document_link': 'DocumentLink',
        'stat_data': 'StatData'
    }

    def __init__(self, request_id=None, document_link=None, stat_data=None):  # noqa: E501
        """StatDataResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._document_link = None
        self._stat_data = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if document_link is not None:
            self.document_link = document_link
        if stat_data is not None:
            self.stat_data = stat_data

    @property
    def request_id(self):
        """Gets the request_id of this StatDataResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this StatDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this StatDataResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this StatDataResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def document_link(self):
        """Gets the document_link of this StatDataResponse.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The document_link of this StatDataResponse.  # noqa: E501
        :rtype: FileLink
        """
        return self._document_link

    @document_link.setter
    def document_link(self, document_link):
        """Sets the document_link of this StatDataResponse.

        Gets or sets the link to the document.  # noqa: E501

        :param document_link: The document_link of this StatDataResponse.  # noqa: E501
        :type: FileLink
        """
        self._document_link = document_link

    @property
    def stat_data(self):
        """Gets the stat_data of this StatDataResponse.  # noqa: E501

        Gets or sets the statistical data of the document.  # noqa: E501

        :return: The stat_data of this StatDataResponse.  # noqa: E501
        :rtype: DocumentStatData
        """
        return self._stat_data

    @stat_data.setter
    def stat_data(self, stat_data):
        """Sets the stat_data of this StatDataResponse.

        Gets or sets the statistical data of the document.  # noqa: E501

        :param stat_data: The stat_data of this StatDataResponse.  # noqa: E501
        :type: DocumentStatData
        """
        self._stat_data = stat_data


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._document_link is not None:
            self._document_link.validate()



        if self._stat_data is not None:
            self._stat_data.validate()


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
        if not isinstance(other, StatDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other