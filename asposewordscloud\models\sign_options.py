# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="sign_options.py">
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

class SignOptions(object):
    """Container class for digital signature options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comments': 'str',
        'decryption_password': 'str',
        'provider_id': 'str',
        'signature_line_id': 'str',
        'signature_line_image_filename': 'str',
        'sign_time': 'datetime'
    }

    attribute_map = {
        'comments': 'Comments',
        'decryption_password': 'DecryptionPassword',
        'provider_id': 'ProviderId',
        'signature_line_id': 'SignatureLineId',
        'signature_line_image_filename': 'SignatureLineImageFilename',
        'sign_time': 'SignTime'
    }

    def __init__(self, comments=None, decryption_password=None, provider_id=None, signature_line_id=None, signature_line_image_filename=None, sign_time=None):  # noqa: E501
        """SignOptions - a model defined in Swagger"""  # noqa: E501

        self._comments = None
        self._decryption_password = None
        self._provider_id = None
        self._signature_line_id = None
        self._signature_line_image_filename = None
        self._sign_time = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if decryption_password is not None:
            self.decryption_password = decryption_password
        if provider_id is not None:
            self.provider_id = provider_id
        if signature_line_id is not None:
            self.signature_line_id = signature_line_id
        if signature_line_image_filename is not None:
            self.signature_line_image_filename = signature_line_image_filename
        if sign_time is not None:
            self.sign_time = sign_time

    @property
    def comments(self):
        """Gets the comments of this SignOptions.  # noqa: E501

        Gets or sets comments on the digital signature. The default value is an empty string.  # noqa: E501

        :return: The comments of this SignOptions.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this SignOptions.

        Gets or sets comments on the digital signature. The default value is an empty string.  # noqa: E501

        :param comments: The comments of this SignOptions.  # noqa: E501
        :type: str
        """
        self._comments = comments

    @property
    def decryption_password(self):
        """Gets the decryption_password of this SignOptions.  # noqa: E501

        Gets or sets the password to decrypt source document. The default value is an empty string.  # noqa: E501

        :return: The decryption_password of this SignOptions.  # noqa: E501
        :rtype: str
        """
        return self._decryption_password

    @decryption_password.setter
    def decryption_password(self, decryption_password):
        """Sets the decryption_password of this SignOptions.

        Gets or sets the password to decrypt source document. The default value is an empty string.  # noqa: E501

        :param decryption_password: The decryption_password of this SignOptions.  # noqa: E501
        :type: str
        """
        self._decryption_password = decryption_password

    @property
    def provider_id(self):
        """Gets the provider_id of this SignOptions.  # noqa: E501

        Gets or sets the class Guid of the signature cryptography provider. The default value is Empty (all zeroes) Guid.  # noqa: E501

        :return: The provider_id of this SignOptions.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this SignOptions.

        Gets or sets the class Guid of the signature cryptography provider. The default value is Empty (all zeroes) Guid.  # noqa: E501

        :param provider_id: The provider_id of this SignOptions.  # noqa: E501
        :type: str
        """
        self._provider_id = provider_id

    @property
    def signature_line_id(self):
        """Gets the signature_line_id of this SignOptions.  # noqa: E501

        Gets or sets user defined signature line Guid. The default value is Empty (all zeroes) Guid.  # noqa: E501

        :return: The signature_line_id of this SignOptions.  # noqa: E501
        :rtype: str
        """
        return self._signature_line_id

    @signature_line_id.setter
    def signature_line_id(self, signature_line_id):
        """Sets the signature_line_id of this SignOptions.

        Gets or sets user defined signature line Guid. The default value is Empty (all zeroes) Guid.  # noqa: E501

        :param signature_line_id: The signature_line_id of this SignOptions.  # noqa: E501
        :type: str
        """
        self._signature_line_id = signature_line_id

    @property
    def signature_line_image_filename(self):
        """Gets the signature_line_image_filename of this SignOptions.  # noqa: E501

        Gets or sets the image that will be shown in associated SignatureLine. The default value is an empty string.  # noqa: E501

        :return: The signature_line_image_filename of this SignOptions.  # noqa: E501
        :rtype: str
        """
        return self._signature_line_image_filename

    @signature_line_image_filename.setter
    def signature_line_image_filename(self, signature_line_image_filename):
        """Sets the signature_line_image_filename of this SignOptions.

        Gets or sets the image that will be shown in associated SignatureLine. The default value is an empty string.  # noqa: E501

        :param signature_line_image_filename: The signature_line_image_filename of this SignOptions.  # noqa: E501
        :type: str
        """
        self._signature_line_image_filename = signature_line_image_filename

    @property
    def sign_time(self):
        """Gets the sign_time of this SignOptions.  # noqa: E501

        Gets or sets the date of signing. The default value is current time (Now).  # noqa: E501

        :return: The sign_time of this SignOptions.  # noqa: E501
        :rtype: datetime
        """
        return self._sign_time

    @sign_time.setter
    def sign_time(self, sign_time):
        """Sets the sign_time of this SignOptions.

        Gets or sets the date of signing. The default value is current time (Now).  # noqa: E501

        :param sign_time: The sign_time of this SignOptions.  # noqa: E501
        :type: datetime
        """
        self._sign_time = sign_time


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
        if not isinstance(other, SignOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other