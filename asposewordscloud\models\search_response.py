# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="search_response.py">
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

class SearchResponse(object):
    """The REST response with a regular expression pattern and a collection of search results. This response is returned by the Service when handling "GET https://api.aspose.cloud/v4.0/words/Test.doc/search" REST API requests.
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
        'searching_pattern': 'str',
        'search_results': 'SearchResultsCollection'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'searching_pattern': 'SearchingPattern',
        'search_results': 'SearchResults'
    }

    def __init__(self, request_id=None, searching_pattern=None, search_results=None):  # noqa: E501
        """SearchResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._searching_pattern = None
        self._search_results = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if searching_pattern is not None:
            self.searching_pattern = searching_pattern
        if search_results is not None:
            self.search_results = search_results

    @property
    def request_id(self):
        """Gets the request_id of this SearchResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this SearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SearchResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this SearchResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def searching_pattern(self):
        """Gets the searching_pattern of this SearchResponse.  # noqa: E501

        Gets or sets the regular expression pattern used to find matches.  # noqa: E501

        :return: The searching_pattern of this SearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._searching_pattern

    @searching_pattern.setter
    def searching_pattern(self, searching_pattern):
        """Sets the searching_pattern of this SearchResponse.

        Gets or sets the regular expression pattern used to find matches.  # noqa: E501

        :param searching_pattern: The searching_pattern of this SearchResponse.  # noqa: E501
        :type: str
        """
        self._searching_pattern = searching_pattern

    @property
    def search_results(self):
        """Gets the search_results of this SearchResponse.  # noqa: E501

        Gets or sets the collection of search results.  # noqa: E501

        :return: The search_results of this SearchResponse.  # noqa: E501
        :rtype: SearchResultsCollection
        """
        return self._search_results

    @search_results.setter
    def search_results(self, search_results):
        """Sets the search_results of this SearchResponse.

        Gets or sets the collection of search results.  # noqa: E501

        :param search_results: The search_results of this SearchResponse.  # noqa: E501
        :type: SearchResultsCollection
        """
        self._search_results = search_results


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._search_results is not None:
            self._search_results.validate()


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
        if not isinstance(other, SearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other