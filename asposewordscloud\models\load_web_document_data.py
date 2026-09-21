# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="load_web_document_data.py">
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

class LoadWebDocumentData(object):
    """Contains data for load web document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'save_options': 'SaveOptionsData',
        'loading_document_url': 'str'
    }

    attribute_map = {
        'save_options': 'SaveOptions',
        'loading_document_url': 'LoadingDocumentUrl'
    }

    def __init__(self, save_options=None, loading_document_url=None):  # noqa: E501
        """LoadWebDocumentData - a model defined in Swagger"""  # noqa: E501

        self._save_options = None
        self._loading_document_url = None
        self.discriminator = None

        if save_options is not None:
            self.save_options = save_options
        if loading_document_url is not None:
            self.loading_document_url = loading_document_url

    @property
    def save_options(self):
        """Gets the save_options of this LoadWebDocumentData.  # noqa: E501

        Gets or sets the save options.  # noqa: E501

        :return: The save_options of this LoadWebDocumentData.  # noqa: E501
        :rtype: SaveOptionsData
        """
        return self._save_options

    @save_options.setter
    def save_options(self, save_options):
        """Sets the save_options of this LoadWebDocumentData.

        Gets or sets the save options.  # noqa: E501

        :param save_options: The save_options of this LoadWebDocumentData.  # noqa: E501
        :type: SaveOptionsData
        """
        self._save_options = save_options

    @property
    def loading_document_url(self):
        """Gets the loading_document_url of this LoadWebDocumentData.  # noqa: E501

        Gets or sets the web document URL.  # noqa: E501

        :return: The loading_document_url of this LoadWebDocumentData.  # noqa: E501
        :rtype: str
        """
        return self._loading_document_url

    @loading_document_url.setter
    def loading_document_url(self, loading_document_url):
        """Sets the loading_document_url of this LoadWebDocumentData.

        Gets or sets the web document URL.  # noqa: E501

        :param loading_document_url: The loading_document_url of this LoadWebDocumentData.  # noqa: E501
        :type: str
        """
        self._loading_document_url = loading_document_url


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._loading_document_url is None:
            raise ValueError("Property LoadingDocumentUrl in LoadWebDocumentData is required.")  # noqa: E501

        if self._save_options is not None:
            self._save_options.validate()



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
        if not isinstance(other, LoadWebDocumentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other