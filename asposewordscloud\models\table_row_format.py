# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_row_format.py">
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

class TableRowFormat(object):
    """DTO container with formatting for a table row.
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
        'height': 'float',
        'height_rule': 'str',
        'allow_break_across_pages': 'bool',
        'heading_format': 'bool'
    }

    attribute_map = {
        'link': 'Link',
        'height': 'Height',
        'height_rule': 'HeightRule',
        'allow_break_across_pages': 'AllowBreakAcrossPages',
        'heading_format': 'HeadingFormat'
    }

    def __init__(self, link=None, height=None, height_rule=None, allow_break_across_pages=None, heading_format=None):  # noqa: E501
        """TableRowFormat - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._height = None
        self._height_rule = None
        self._allow_break_across_pages = None
        self._heading_format = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if height is not None:
            self.height = height
        if height_rule is not None:
            self.height_rule = height_rule
        if allow_break_across_pages is not None:
            self.allow_break_across_pages = allow_break_across_pages
        if heading_format is not None:
            self.heading_format = heading_format

    @property
    def link(self):
        """Gets the link of this TableRowFormat.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this TableRowFormat.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TableRowFormat.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this TableRowFormat.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def height(self):
        """Gets the height of this TableRowFormat.  # noqa: E501

        Gets or sets the height of the table row in points.  # noqa: E501

        :return: The height of this TableRowFormat.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TableRowFormat.

        Gets or sets the height of the table row in points.  # noqa: E501

        :param height: The height of this TableRowFormat.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def height_rule(self):
        """Gets the height_rule of this TableRowFormat.  # noqa: E501

        Gets or sets the rule for determining the height of the table row.  # noqa: E501

        :return: The height_rule of this TableRowFormat.  # noqa: E501
        :rtype: str
        """
        return self._height_rule

    @height_rule.setter
    def height_rule(self, height_rule):
        """Sets the height_rule of this TableRowFormat.

        Gets or sets the rule for determining the height of the table row.  # noqa: E501

        :param height_rule: The height_rule of this TableRowFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["AtLeast", "Exactly", "Auto"]  # noqa: E501
        if not height_rule.isdigit():
            if height_rule not in allowed_values:
                raise ValueError(
                    "Invalid value for `height_rule` ({0}), must be one of {1}"  # noqa: E501
                    .format(height_rule, allowed_values))
            self._height_rule = height_rule
        else:
            self._height_rule = allowed_values[int(height_rule) if six.PY3 else long(height_rule)]

    @property
    def allow_break_across_pages(self):
        """Gets the allow_break_across_pages of this TableRowFormat.  # noqa: E501

        Gets or sets a value indicating whether the text in a table row is allowed to split across a page break.  # noqa: E501

        :return: The allow_break_across_pages of this TableRowFormat.  # noqa: E501
        :rtype: bool
        """
        return self._allow_break_across_pages

    @allow_break_across_pages.setter
    def allow_break_across_pages(self, allow_break_across_pages):
        """Sets the allow_break_across_pages of this TableRowFormat.

        Gets or sets a value indicating whether the text in a table row is allowed to split across a page break.  # noqa: E501

        :param allow_break_across_pages: The allow_break_across_pages of this TableRowFormat.  # noqa: E501
        :type: bool
        """
        self._allow_break_across_pages = allow_break_across_pages

    @property
    def heading_format(self):
        """Gets the heading_format of this TableRowFormat.  # noqa: E501

        Gets or sets a value indicating whether the row is repeated as a table heading on every page when the table spans more than one page.  # noqa: E501

        :return: The heading_format of this TableRowFormat.  # noqa: E501
        :rtype: bool
        """
        return self._heading_format

    @heading_format.setter
    def heading_format(self, heading_format):
        """Sets the heading_format of this TableRowFormat.

        Gets or sets a value indicating whether the row is repeated as a table heading on every page when the table spans more than one page.  # noqa: E501

        :param heading_format: The heading_format of this TableRowFormat.  # noqa: E501
        :type: bool
        """
        self._heading_format = heading_format


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

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
        if not isinstance(other, TableRowFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other