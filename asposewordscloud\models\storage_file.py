# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="storage_file.py">
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

class StorageFile(object):
    """File or folder information.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_folder': 'bool',
        'modified_date': 'datetime',
        'name': 'str',
        'path': 'str',
        'size': 'int'
    }

    attribute_map = {
        'is_folder': 'IsFolder',
        'modified_date': 'ModifiedDate',
        'name': 'Name',
        'path': 'Path',
        'size': 'Size'
    }

    def __init__(self, is_folder=None, modified_date=None, name=None, path=None, size=None):  # noqa: E501
        """StorageFile - a model defined in Swagger"""  # noqa: E501

        self._is_folder = None
        self._modified_date = None
        self._name = None
        self._path = None
        self._size = None
        self.discriminator = None

        if is_folder is not None:
            self.is_folder = is_folder
        if modified_date is not None:
            self.modified_date = modified_date
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if size is not None:
            self.size = size

    @property
    def is_folder(self):
        """Gets the is_folder of this StorageFile.  # noqa: E501

        True if it is a folder.  # noqa: E501

        :return: The is_folder of this StorageFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this StorageFile.

        True if it is a folder.  # noqa: E501

        :param is_folder: The is_folder of this StorageFile.  # noqa: E501
        :type: bool
        """
        self._is_folder = is_folder

    @property
    def modified_date(self):
        """Gets the modified_date of this StorageFile.  # noqa: E501

        File or folder last modified DateTime.  # noqa: E501

        :return: The modified_date of this StorageFile.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this StorageFile.

        File or folder last modified DateTime.  # noqa: E501

        :param modified_date: The modified_date of this StorageFile.  # noqa: E501
        :type: datetime
        """
        self._modified_date = modified_date

    @property
    def name(self):
        """Gets the name of this StorageFile.  # noqa: E501

        File or folder name.  # noqa: E501

        :return: The name of this StorageFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageFile.

        File or folder name.  # noqa: E501

        :param name: The name of this StorageFile.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this StorageFile.  # noqa: E501

        File or folder path.  # noqa: E501

        :return: The path of this StorageFile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this StorageFile.

        File or folder path.  # noqa: E501

        :param path: The path of this StorageFile.  # noqa: E501
        :type: str
        """
        self._path = path

    @property
    def size(self):
        """Gets the size of this StorageFile.  # noqa: E501

        File or folder size.  # noqa: E501

        :return: The size of this StorageFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this StorageFile.

        File or folder size.  # noqa: E501

        :param size: The size of this StorageFile.  # noqa: E501
        :type: int
        """
        self._size = size


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._is_folder is None:
            raise ValueError("Property IsFolder in StorageFile is required.")  # noqa: E501
        if self._size is None:
            raise ValueError("Property Size in StorageFile is required.")  # noqa: E501

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
        if not isinstance(other, StorageFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other