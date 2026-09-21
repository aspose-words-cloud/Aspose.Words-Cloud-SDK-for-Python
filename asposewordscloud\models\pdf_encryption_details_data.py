# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="pdf_encryption_details_data.py">
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

class PdfEncryptionDetailsData(object):
    """Container class for details of encryption.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'owner_password': 'str',
        'permissions': 'list[str]',
        'user_password': 'str'
    }

    attribute_map = {
        'owner_password': 'OwnerPassword',
        'permissions': 'Permissions',
        'user_password': 'UserPassword'
    }

    def __init__(self, owner_password=None, permissions=None, user_password=None):  # noqa: E501
        """PdfEncryptionDetailsData - a model defined in Swagger"""  # noqa: E501

        self._owner_password = None
        self._permissions = None
        self._user_password = None
        self.discriminator = None

        if owner_password is not None:
            self.owner_password = owner_password
        if permissions is not None:
            self.permissions = permissions
        if user_password is not None:
            self.user_password = user_password

    @property
    def owner_password(self):
        """Gets the owner_password of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets the owner password for the encrypted PDF document.  # noqa: E501

        :return: The owner_password of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._owner_password

    @owner_password.setter
    def owner_password(self, owner_password):
        """Sets the owner_password of this PdfEncryptionDetailsData.

        Gets or sets the owner password for the encrypted PDF document.  # noqa: E501

        :param owner_password: The owner_password of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._owner_password = owner_password

    @property
    def permissions(self):
        """Gets the permissions of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets the operations that are allowed to a user on the encrypted PDF document.  # noqa: E501

        :return: The permissions of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this PdfEncryptionDetailsData.

        Gets or sets the operations that are allowed to a user on the encrypted PDF document.  # noqa: E501

        :param permissions: The permissions of this PdfEncryptionDetailsData.  # noqa: E501
        :type: list[str]
        """
        self._permissions = permissions

    @property
    def user_password(self):
        """Gets the user_password of this PdfEncryptionDetailsData.  # noqa: E501

        Gets or sets the user password required for opening the encrypted PDF document.  # noqa: E501

        :return: The user_password of this PdfEncryptionDetailsData.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this PdfEncryptionDetailsData.

        Gets or sets the user password required for opening the encrypted PDF document.  # noqa: E501

        :param user_password: The user_password of this PdfEncryptionDetailsData.  # noqa: E501
        :type: str
        """
        self._user_password = user_password


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
        if not isinstance(other, PdfEncryptionDetailsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other