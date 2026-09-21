# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="document_property.py">
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

class DocumentProperty(object):
    """Words document property DTO.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'name': 'str',
        'value': 'str',
        'built_in': 'bool'
    }

    attribute_map = {
        'link': 'Link',
        'name': 'Name',
        'value': 'Value',
        'built_in': 'BuiltIn'
    }

    def __init__(self, link=None, name=None, value=None, built_in=None):  # noqa: E501
        """DocumentProperty - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._name = None
        self._value = None
        self._built_in = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if built_in is not None:
            self.built_in = built_in

    @property
    def link(self):
        """Gets the link of this DocumentProperty.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this DocumentProperty.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DocumentProperty.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this DocumentProperty.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def name(self):
        """Gets the name of this DocumentProperty.  # noqa: E501

        Gets or sets the name of the document property.  # noqa: E501

        :return: The name of this DocumentProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentProperty.

        Gets or sets the name of the document property.  # noqa: E501

        :param name: The name of this DocumentProperty.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this DocumentProperty.  # noqa: E501

        Gets or sets the value of the document property.  # noqa: E501

        :return: The value of this DocumentProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DocumentProperty.

        Gets or sets the value of the document property.  # noqa: E501

        :param value: The value of this DocumentProperty.  # noqa: E501
        :type: str
        """
        self._value = value

    @property
    def built_in(self):
        """Gets the built_in of this DocumentProperty.  # noqa: E501

        Gets or sets a value indicating whether the property is built-in or not. If true the property is built-in, if false the property is custom.  # noqa: E501

        :return: The built_in of this DocumentProperty.  # noqa: E501
        :rtype: bool
        """
        return self._built_in

    @built_in.setter
    def built_in(self, built_in):
        """Sets the built_in of this DocumentProperty.

        Gets or sets a value indicating whether the property is built-in or not. If true the property is built-in, if false the property is custom.  # noqa: E501

        :param built_in: The built_in of this DocumentProperty.  # noqa: E501
        :type: bool
        """
        self._built_in = built_in


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._built_in is None:
            raise ValueError("Property BuiltIn in DocumentProperty is required.")  # noqa: E501

        if self._link is not None:
            self._link.validate()





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
        if not isinstance(other, DocumentProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other