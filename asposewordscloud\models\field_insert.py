# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="field_insert.py">
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

class FieldInsert(object):
    """Field for insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'locale_id': 'str',
        'field_code': 'str',
        'position': 'Position'
    }

    attribute_map = {
        'locale_id': 'LocaleId',
        'field_code': 'FieldCode',
        'position': 'Position'
    }

    def __init__(self, locale_id=None, field_code=None, position=None):  # noqa: E501
        """FieldInsert - a model defined in Swagger"""  # noqa: E501

        self._locale_id = None
        self._field_code = None
        self._position = None
        self.discriminator = None

        if locale_id is not None:
            self.locale_id = locale_id
        if field_code is not None:
            self.field_code = field_code
        if position is not None:
            self.position = position

    @property
    def locale_id(self):
        """Gets the locale_id of this FieldInsert.  # noqa: E501

        Gets or sets the LCID of the field.  # noqa: E501

        :return: The locale_id of this FieldInsert.  # noqa: E501
        :rtype: str
        """
        return self._locale_id

    @locale_id.setter
    def locale_id(self, locale_id):
        """Sets the locale_id of this FieldInsert.

        Gets or sets the LCID of the field.  # noqa: E501

        :param locale_id: The locale_id of this FieldInsert.  # noqa: E501
        :type: str
        """
        self._locale_id = locale_id

    @property
    def field_code(self):
        """Gets the field_code of this FieldInsert.  # noqa: E501

        Gets or sets the field code.  # noqa: E501

        :return: The field_code of this FieldInsert.  # noqa: E501
        :rtype: str
        """
        return self._field_code

    @field_code.setter
    def field_code(self, field_code):
        """Sets the field_code of this FieldInsert.

        Gets or sets the field code.  # noqa: E501

        :param field_code: The field_code of this FieldInsert.  # noqa: E501
        :type: str
        """
        self._field_code = field_code

    @property
    def position(self):
        """Gets the position of this FieldInsert.  # noqa: E501

        Gets or sets the position of the node that will be used to determine the placement of a new field.  # noqa: E501

        :return: The position of this FieldInsert.  # noqa: E501
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this FieldInsert.

        Gets or sets the position of the node that will be used to determine the placement of a new field.  # noqa: E501

        :param position: The position of this FieldInsert.  # noqa: E501
        :type: Position
        """
        self._position = position


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._field_code is None:
            raise ValueError("Property FieldCode in FieldInsert is required.")  # noqa: E501

        if self._position is not None:
            self._position.validate()


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
        if not isinstance(other, FieldInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other