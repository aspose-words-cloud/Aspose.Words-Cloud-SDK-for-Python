# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="file_reference.py">
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

import datetime
import six
import json
import uuid

class FileReference(object):
    swagger_types = {
        'source': 'str',
        'reference': 'str',
        'password': 'str',
        'encryptedPassword': 'str'
    }

    attribute_map = {
        'source': 'Source',
        'reference': 'Reference',
        'password': 'Password',
        'encryptedPassword': 'EncryptedPassword'
    }

    def __init__(self, source, reference, content, password):  # noqa: E501
        self._source = source
        self._reference = reference
        self._content = content
        self._password = password
        self._encryptedPassword = None

    @staticmethod
    def fromRemoteFilePath(remoteFilePath, password = None):
        return FileReference('Storage', remoteFilePath, None, password)

    @staticmethod
    def fromLocalFileContent(localFileContent, password = None):
        return FileReference('Request', str(uuid.uuid4()), localFileContent, password)

    @property
    def source(self):
        return self._source

    @property
    def reference(self):
        return self._reference

    @property
    def content(self):
        return self._content

    @property
    def password(self):
        return self._password

    @property
    def encryptedPassword(self):
        return self._encryptedPassword

    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""
        if self._source == 'Request':
            filesContentResult.append(self)

    def encryptPassword(self, encryptor):
        if self._password is not None:
            self._encryptedPassword = encryptor.encrypt(self._password)
            self._password = None

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