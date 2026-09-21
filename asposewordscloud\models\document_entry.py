# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="document_entry.py">
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

class DocumentEntry(object):
    """Represents a document which will be appended to the original resource document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_reference': 'FileReference',
        'encrypted_password': 'str',
        'import_format_mode': 'str'
    }

    attribute_map = {
        'file_reference': 'FileReference',
        'encrypted_password': 'EncryptedPassword',
        'import_format_mode': 'ImportFormatMode'
    }

    def __init__(self, file_reference=None, encrypted_password=None, import_format_mode=None):  # noqa: E501
        """DocumentEntry - a model defined in Swagger"""  # noqa: E501

        self._file_reference = None
        self._encrypted_password = None
        self._import_format_mode = None
        self.discriminator = None

        if file_reference is not None:
            self.file_reference = file_reference
        if encrypted_password is not None:
            self.encrypted_password = encrypted_password
        if import_format_mode is not None:
            self.import_format_mode = import_format_mode

    @property
    def file_reference(self):
        """Gets the file_reference of this DocumentEntry.  # noqa: E501

        Gets or sets the file reference.  # noqa: E501

        :return: The file_reference of this DocumentEntry.  # noqa: E501
        :rtype: FileReference
        """
        return self._file_reference

    @file_reference.setter
    def file_reference(self, file_reference):
        """Sets the file_reference of this DocumentEntry.

        Gets or sets the file reference.  # noqa: E501

        :param file_reference: The file_reference of this DocumentEntry.  # noqa: E501
        :type: FileReference
        """
        self._file_reference = file_reference

    @property
    def encrypted_password(self):
        """Gets the encrypted_password of this DocumentEntry.  # noqa: E501

        Gets or sets document password encrypted on API public key. The default value is null (the document has no password).  # noqa: E501

        :return: The encrypted_password of this DocumentEntry.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_password

    @encrypted_password.setter
    def encrypted_password(self, encrypted_password):
        """Sets the encrypted_password of this DocumentEntry.

        Gets or sets document password encrypted on API public key. The default value is null (the document has no password).  # noqa: E501

        :param encrypted_password: The encrypted_password of this DocumentEntry.  # noqa: E501
        :type: str
        """
        self._encrypted_password = encrypted_password

    @property
    def import_format_mode(self):
        """Gets the import_format_mode of this DocumentEntry.  # noqa: E501

        Gets or sets the option that controls formatting will be used: appended or destination document. Can be KeepSourceFormatting or UseDestinationStyles.  # noqa: E501

        :return: The import_format_mode of this DocumentEntry.  # noqa: E501
        :rtype: str
        """
        return self._import_format_mode

    @import_format_mode.setter
    def import_format_mode(self, import_format_mode):
        """Sets the import_format_mode of this DocumentEntry.

        Gets or sets the option that controls formatting will be used: appended or destination document. Can be KeepSourceFormatting or UseDestinationStyles.  # noqa: E501

        :param import_format_mode: The import_format_mode of this DocumentEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["UseDestinationStyles", "KeepSourceFormatting", "KeepDifferentStyles"]  # noqa: E501
        if not import_format_mode.isdigit():
            if import_format_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `import_format_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(import_format_mode, allowed_values))
            self._import_format_mode = import_format_mode
        else:
            self._import_format_mode = allowed_values[int(import_format_mode) if six.PY3 else long(import_format_mode)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""
        if self._file_reference is not None:
            self._file_reference.extract_files_content(filesContentResult)




    def validate(self):
        """Validate all required properties in model"""
        if self._file_reference is None:
            raise ValueError("Property FileReference in DocumentEntry is required.")  # noqa: E501
        if self._import_format_mode is None:
            raise ValueError("Property ImportFormatMode in DocumentEntry is required.")  # noqa: E501

        if self._file_reference is not None:
            self._file_reference.validate()




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
        if not isinstance(other, DocumentEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other