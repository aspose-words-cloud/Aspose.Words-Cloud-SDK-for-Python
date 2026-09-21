# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_row_insert.py">
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

class TableRowInsert(object):
    """DTO container with a table row element.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'columns_count': 'int',
        'existing_row_position': 'Position',
        'insert_after': 'int'
    }

    attribute_map = {
        'columns_count': 'ColumnsCount',
        'existing_row_position': 'ExistingRowPosition',
        'insert_after': 'InsertAfter'
    }

    def __init__(self, columns_count=None, existing_row_position=None, insert_after=None):  # noqa: E501
        """TableRowInsert - a model defined in Swagger"""  # noqa: E501

        self._columns_count = None
        self._existing_row_position = None
        self._insert_after = None
        self.discriminator = None

        if columns_count is not None:
            self.columns_count = columns_count
        if existing_row_position is not None:
            self.existing_row_position = existing_row_position
        if insert_after is not None:
            self.insert_after = insert_after

    @property
    def columns_count(self):
        """Gets the columns_count of this TableRowInsert.  # noqa: E501

        Gets or sets the count of columns. The default value is 1.  # noqa: E501

        :return: The columns_count of this TableRowInsert.  # noqa: E501
        :rtype: int
        """
        return self._columns_count

    @columns_count.setter
    def columns_count(self, columns_count):
        """Sets the columns_count of this TableRowInsert.

        Gets or sets the count of columns. The default value is 1.  # noqa: E501

        :param columns_count: The columns_count of this TableRowInsert.  # noqa: E501
        :type: int
        """
        self._columns_count = columns_count

    @property
    def existing_row_position(self):
        """Gets the existing_row_position of this TableRowInsert.  # noqa: E501

        Gets or sets the position of the table row that will be used to determine the placement of a new row.  # noqa: E501

        :return: The existing_row_position of this TableRowInsert.  # noqa: E501
        :rtype: Position
        """
        return self._existing_row_position

    @existing_row_position.setter
    def existing_row_position(self, existing_row_position):
        """Sets the existing_row_position of this TableRowInsert.

        Gets or sets the position of the table row that will be used to determine the placement of a new row.  # noqa: E501

        :param existing_row_position: The existing_row_position of this TableRowInsert.  # noqa: E501
        :type: Position
        """
        self._existing_row_position = existing_row_position

    @property
    def insert_after(self):
        """Gets the insert_after of this TableRowInsert.  # noqa: E501

        Gets or sets table row will be inserted after row with specified 0-based index.  # noqa: E501

        :return: The insert_after of this TableRowInsert.  # noqa: E501
        :rtype: int
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this TableRowInsert.

        Gets or sets table row will be inserted after row with specified 0-based index.  # noqa: E501

        :param insert_after: The insert_after of this TableRowInsert.  # noqa: E501
        :type: int
        """
        self._insert_after = insert_after


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._columns_count is None:
            raise ValueError("Property ColumnsCount in TableRowInsert is required.")  # noqa: E501

        if self._existing_row_position is not None:
            self._existing_row_position.validate()



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
        if not isinstance(other, TableRowInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other