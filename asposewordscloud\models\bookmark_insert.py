# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="bookmark_insert.py">
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

class BookmarkInsert(object):
    """Represents a bookmark to insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'text': 'str',
        'start_range': 'Position',
        'end_range': 'Position'
    }

    attribute_map = {
        'name': 'Name',
        'text': 'Text',
        'start_range': 'StartRange',
        'end_range': 'EndRange'
    }

    def __init__(self, name=None, text=None, start_range=None, end_range=None):  # noqa: E501
        """BookmarkInsert - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._text = None
        self._start_range = None
        self._end_range = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if text is not None:
            self.text = text
        if start_range is not None:
            self.start_range = start_range
        if end_range is not None:
            self.end_range = end_range

    @property
    def name(self):
        """Gets the name of this BookmarkInsert.  # noqa: E501

        Gets or sets the name of the bookmark.  # noqa: E501

        :return: The name of this BookmarkInsert.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BookmarkInsert.

        Gets or sets the name of the bookmark.  # noqa: E501

        :param name: The name of this BookmarkInsert.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def text(self):
        """Gets the text of this BookmarkInsert.  # noqa: E501

        Gets or sets text, enclosed in the bookmark.  # noqa: E501

        :return: The text of this BookmarkInsert.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this BookmarkInsert.

        Gets or sets text, enclosed in the bookmark.  # noqa: E501

        :param text: The text of this BookmarkInsert.  # noqa: E501
        :type: str
        """
        self._text = text

    @property
    def start_range(self):
        """Gets the start_range of this BookmarkInsert.  # noqa: E501

        Gets or sets the link to start bookmark node.  # noqa: E501

        :return: The start_range of this BookmarkInsert.  # noqa: E501
        :rtype: Position
        """
        return self._start_range

    @start_range.setter
    def start_range(self, start_range):
        """Sets the start_range of this BookmarkInsert.

        Gets or sets the link to start bookmark node.  # noqa: E501

        :param start_range: The start_range of this BookmarkInsert.  # noqa: E501
        :type: Position
        """
        self._start_range = start_range

    @property
    def end_range(self):
        """Gets the end_range of this BookmarkInsert.  # noqa: E501

        Gets or sets the link to end bookmark node.  # noqa: E501

        :return: The end_range of this BookmarkInsert.  # noqa: E501
        :rtype: Position
        """
        return self._end_range

    @end_range.setter
    def end_range(self, end_range):
        """Sets the end_range of this BookmarkInsert.

        Gets or sets the link to end bookmark node.  # noqa: E501

        :param end_range: The end_range of this BookmarkInsert.  # noqa: E501
        :type: Position
        """
        self._end_range = end_range


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._name is None:
            raise ValueError("Property Name in BookmarkInsert is required.")  # noqa: E501
        if self._text is None:
            raise ValueError("Property Text in BookmarkInsert is required.")  # noqa: E501
        if self._start_range is None:
            raise ValueError("Property StartRange in BookmarkInsert is required.")  # noqa: E501
        if self._end_range is None:
            raise ValueError("Property EndRange in BookmarkInsert is required.")  # noqa: E501

        if self._start_range is not None:
            self._start_range.validate()



        if self._end_range is not None:
            self._end_range.validate()


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
        if not isinstance(other, BookmarkInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other