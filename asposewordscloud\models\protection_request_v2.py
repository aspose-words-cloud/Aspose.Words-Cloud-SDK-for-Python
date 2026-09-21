# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="protection_request_v2.py">
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

class ProtectionRequestV2(object):
    """Request on changing of protection.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'protection_password': 'str',
        'protection_type': 'str'
    }

    attribute_map = {
        'protection_password': 'ProtectionPassword',
        'protection_type': 'ProtectionType'
    }

    def __init__(self, protection_password=None, protection_type=None):  # noqa: E501
        """ProtectionRequestV2 - a model defined in Swagger"""  # noqa: E501

        self._protection_password = None
        self._protection_type = None
        self.discriminator = None

        if protection_password is not None:
            self.protection_password = protection_password
        if protection_type is not None:
            self.protection_type = protection_type

    @property
    def protection_password(self):
        """Gets the protection_password of this ProtectionRequestV2.  # noqa: E501

        Gets or sets the new password for the document protection. This property is required, but empty value is allowed.  # noqa: E501

        :return: The protection_password of this ProtectionRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._protection_password

    @protection_password.setter
    def protection_password(self, protection_password):
        """Sets the protection_password of this ProtectionRequestV2.

        Gets or sets the new password for the document protection. This property is required, but empty value is allowed.  # noqa: E501

        :param protection_password: The protection_password of this ProtectionRequestV2.  # noqa: E501
        :type: str
        """
        self._protection_password = protection_password

    @property
    def protection_type(self):
        """Gets the protection_type of this ProtectionRequestV2.  # noqa: E501

        Gets or sets the new type of the document protection.  # noqa: E501

        :return: The protection_type of this ProtectionRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this ProtectionRequestV2.

        Gets or sets the new type of the document protection.  # noqa: E501

        :param protection_type: The protection_type of this ProtectionRequestV2.  # noqa: E501
        :type: str
        """
        allowed_values = ["AllowOnlyRevisions", "AllowOnlyComments", "AllowOnlyFormFields", "ReadOnly", "NoProtection"]  # noqa: E501
        if not protection_type.isdigit():
            if protection_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `protection_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(protection_type, allowed_values))
            self._protection_type = protection_type
        else:
            self._protection_type = allowed_values[int(protection_type) if six.PY3 else long(protection_type)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._protection_password is None:
            raise ValueError("Property ProtectionPassword in ProtectionRequestV2 is required.")  # noqa: E501
        if self._protection_type is None:
            raise ValueError("Property ProtectionType in ProtectionRequestV2 is required.")  # noqa: E501

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
        if not isinstance(other, ProtectionRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other