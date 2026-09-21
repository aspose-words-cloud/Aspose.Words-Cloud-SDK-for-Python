# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_cell_insert.py">
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

class TableCellInsert(object):
    """DTO container with a table cell.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'existing_cell_position': 'Position',
        'insert_after': 'int'
    }

    attribute_map = {
        'existing_cell_position': 'ExistingCellPosition',
        'insert_after': 'InsertAfter'
    }

    def __init__(self, existing_cell_position=None, insert_after=None):  # noqa: E501
        """TableCellInsert - a model defined in Swagger"""  # noqa: E501

        self._existing_cell_position = None
        self._insert_after = None
        self.discriminator = None

        if existing_cell_position is not None:
            self.existing_cell_position = existing_cell_position
        if insert_after is not None:
            self.insert_after = insert_after

    @property
    def existing_cell_position(self):
        """Gets the existing_cell_position of this TableCellInsert.  # noqa: E501

        Gets or sets the position of the table cell that will be used to determine the placement of a new cell.  # noqa: E501

        :return: The existing_cell_position of this TableCellInsert.  # noqa: E501
        :rtype: Position
        """
        return self._existing_cell_position

    @existing_cell_position.setter
    def existing_cell_position(self, existing_cell_position):
        """Sets the existing_cell_position of this TableCellInsert.

        Gets or sets the position of the table cell that will be used to determine the placement of a new cell.  # noqa: E501

        :param existing_cell_position: The existing_cell_position of this TableCellInsert.  # noqa: E501
        :type: Position
        """
        self._existing_cell_position = existing_cell_position

    @property
    def insert_after(self):
        """Gets the insert_after of this TableCellInsert.  # noqa: E501

        Gets or sets the 0-based index, the table cell will be inserted after.  # noqa: E501

        :return: The insert_after of this TableCellInsert.  # noqa: E501
        :rtype: int
        """
        return self._insert_after

    @insert_after.setter
    def insert_after(self, insert_after):
        """Sets the insert_after of this TableCellInsert.

        Gets or sets the 0-based index, the table cell will be inserted after.  # noqa: E501

        :param insert_after: The insert_after of this TableCellInsert.  # noqa: E501
        :type: int
        """
        self._insert_after = insert_after


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._existing_cell_position is not None:
            self._existing_cell_position.validate()



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
        if not isinstance(other, TableCellInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other