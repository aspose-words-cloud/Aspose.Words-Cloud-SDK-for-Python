# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="file_link.py">
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

class FileLink(object):
    """Provides information for the file link.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'rel': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'href': 'Href',
        'rel': 'Rel',
        'title': 'Title',
        'type': 'Type'
    }

    def __init__(self, href=None, rel=None, title=None, type=None):  # noqa: E501
        """FileLink - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._rel = None
        self._title = None
        self._type = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def href(self):
        """Gets the href of this FileLink.  # noqa: E501

        Gets or sets the "href" attribute with the link's IRI. atom:link elements MUST have an href attribute, whose value MUST be a IRI reference.  # noqa: E501

        :return: The href of this FileLink.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FileLink.

        Gets or sets the "href" attribute with the link's IRI. atom:link elements MUST have an href attribute, whose value MUST be a IRI reference.  # noqa: E501

        :param href: The href of this FileLink.  # noqa: E501
        :type: str
        """
        self._href = href

    @property
    def rel(self):
        """Gets the rel of this FileLink.  # noqa: E501

        Gets or sets the option that controls whether atom:link elements MAY have a "rel" attribute that indicates the link relation type.  If the "rel" attribute is not present, the link element MUST be interpreted as if the link relation type is "alternate".  # noqa: E501

        :return: The rel of this FileLink.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this FileLink.

        Gets or sets the option that controls whether atom:link elements MAY have a "rel" attribute that indicates the link relation type.  If the "rel" attribute is not present, the link element MUST be interpreted as if the link relation type is "alternate".  # noqa: E501

        :param rel: The rel of this FileLink.  # noqa: E501
        :type: str
        """
        self._rel = rel

    @property
    def title(self):
        """Gets the title of this FileLink.  # noqa: E501

        Gets or sets the "title" attribute, that conveys human-readable information about the link. The content of the "title" attribute is Language-Sensitive.  # noqa: E501

        :return: The title of this FileLink.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FileLink.

        Gets or sets the "title" attribute, that conveys human-readable information about the link. The content of the "title" attribute is Language-Sensitive.  # noqa: E501

        :param title: The title of this FileLink.  # noqa: E501
        :type: str
        """
        self._title = title

    @property
    def type(self):
        """Gets the type of this FileLink.  # noqa: E501

        Gets or sets the "type" attribute. The "type" attribute's value is an advisory media type: it is a hint about the type of the representation that is expected to be returned when the value of the href attribute is dereferenced. Note that the type attribute does not override the actual media type returned with the representation.  # noqa: E501

        :return: The type of this FileLink.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileLink.

        Gets or sets the "type" attribute. The "type" attribute's value is an advisory media type: it is a hint about the type of the representation that is expected to be returned when the value of the href attribute is dereferenced. Note that the type attribute does not override the actual media type returned with the representation.  # noqa: E501

        :param type: The type of this FileLink.  # noqa: E501
        :type: str
        """
        self._type = type


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
        if not isinstance(other, FileLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other