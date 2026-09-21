# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="tab_stop_insert.py">
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

class TabStopInsert(object):
    """A DTO to Insert / replace a tab stop.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alignment': 'str',
        'leader': 'str',
        'position': 'float'
    }

    attribute_map = {
        'alignment': 'Alignment',
        'leader': 'Leader',
        'position': 'Position'
    }

    def __init__(self, alignment=None, leader=None, position=None):  # noqa: E501
        """TabStopInsert - a model defined in Swagger"""  # noqa: E501

        self._alignment = None
        self._leader = None
        self._position = None
        self.discriminator = None

        if alignment is not None:
            self.alignment = alignment
        if leader is not None:
            self.leader = leader
        if position is not None:
            self.position = position

    @property
    def alignment(self):
        """Gets the alignment of this TabStopInsert.  # noqa: E501

        Gets or sets the alignment of text at this tab stop.  # noqa: E501

        :return: The alignment of this TabStopInsert.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this TabStopInsert.

        Gets or sets the alignment of text at this tab stop.  # noqa: E501

        :param alignment: The alignment of this TabStopInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Left", "Center", "Right", "Decimal", "Bar", "List", "Clear"]  # noqa: E501
        if not alignment.isdigit():
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values))
            self._alignment = alignment
        else:
            self._alignment = allowed_values[int(alignment) if six.PY3 else long(alignment)]

    @property
    def leader(self):
        """Gets the leader of this TabStopInsert.  # noqa: E501

        Gets or sets the type of the leader line displayed under the tab character.  # noqa: E501

        :return: The leader of this TabStopInsert.  # noqa: E501
        :rtype: str
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        """Sets the leader of this TabStopInsert.

        Gets or sets the type of the leader line displayed under the tab character.  # noqa: E501

        :param leader: The leader of this TabStopInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Dots", "Dashes", "Line", "Heavy", "MiddleDot"]  # noqa: E501
        if not leader.isdigit():
            if leader not in allowed_values:
                raise ValueError(
                    "Invalid value for `leader` ({0}), must be one of {1}"  # noqa: E501
                    .format(leader, allowed_values))
            self._leader = leader
        else:
            self._leader = allowed_values[int(leader) if six.PY3 else long(leader)]

    @property
    def position(self):
        """Gets the position of this TabStopInsert.  # noqa: E501

        Gets or sets the position of the tab stop in points.  # noqa: E501

        :return: The position of this TabStopInsert.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TabStopInsert.

        Gets or sets the position of the tab stop in points.  # noqa: E501

        :param position: The position of this TabStopInsert.  # noqa: E501
        :type: float
        """
        self._position = position


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._alignment is None:
            raise ValueError("Property Alignment in TabStopInsert is required.")  # noqa: E501
        if self._leader is None:
            raise ValueError("Property Leader in TabStopInsert is required.")  # noqa: E501
        if self._position is None:
            raise ValueError("Property Position in TabStopInsert is required.")  # noqa: E501

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
        if not isinstance(other, TabStopInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other