# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="signature.py">
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

class Signature(object):
    """The REST response with a document signature collection. This response is returned by the Service when handling any "https://api.aspose.cloud/v4.0/words/Test.doc/signatures" REST API requests.
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
        'issuer_name': 'str',
        'is_valid': 'bool',
        'signature_type': 'str',
        'signature_value': 'str',
        'sign_time': 'datetime',
        'subject_name': 'str'
    }

    attribute_map = {
        'comments': 'Comments',
        'issuer_name': 'IssuerName',
        'is_valid': 'IsValid',
        'signature_type': 'SignatureType',
        'signature_value': 'SignatureValue',
        'sign_time': 'SignTime',
        'subject_name': 'SubjectName'
    }

    def __init__(self, comments=None, issuer_name=None, is_valid=None, signature_type=None, signature_value=None, sign_time=None, subject_name=None):  # noqa: E501
        """Signature - a model defined in Swagger"""  # noqa: E501

        self._comments = None
        self._issuer_name = None
        self._is_valid = None
        self._signature_type = None
        self._signature_value = None
        self._sign_time = None
        self._subject_name = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if is_valid is not None:
            self.is_valid = is_valid
        if signature_type is not None:
            self.signature_type = signature_type
        if signature_value is not None:
            self.signature_value = signature_value
        if sign_time is not None:
            self.sign_time = sign_time
        if subject_name is not None:
            self.subject_name = subject_name

    @property
    def comments(self):
        """Gets the comments of this Signature.  # noqa: E501

        Gets or sets the signing purpose comment.  # noqa: E501

        :return: The comments of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Signature.

        Gets or sets the signing purpose comment.  # noqa: E501

        :param comments: The comments of this Signature.  # noqa: E501
        :type: str
        """
        self._comments = comments

    @property
    def issuer_name(self):
        """Gets the issuer_name of this Signature.  # noqa: E501

        Gets or sets the subject distinguished name of the certificate issuer.  # noqa: E501

        :return: The issuer_name of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this Signature.

        Gets or sets the subject distinguished name of the certificate issuer.  # noqa: E501

        :param issuer_name: The issuer_name of this Signature.  # noqa: E501
        :type: str
        """
        self._issuer_name = issuer_name

    @property
    def is_valid(self):
        """Gets the is_valid of this Signature.  # noqa: E501

        Gets or sets a value indicating whether this digital signature is valid.  # noqa: E501

        :return: The is_valid of this Signature.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this Signature.

        Gets or sets a value indicating whether this digital signature is valid.  # noqa: E501

        :param is_valid: The is_valid of this Signature.  # noqa: E501
        :type: bool
        """
        self._is_valid = is_valid

    @property
    def signature_type(self):
        """Gets the signature_type of this Signature.  # noqa: E501

        Gets or sets the type of the digital signature.  # noqa: E501

        :return: The signature_type of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this Signature.

        Gets or sets the type of the digital signature.  # noqa: E501

        :param signature_type: The signature_type of this Signature.  # noqa: E501
        :type: str
        """
        self._signature_type = signature_type

    @property
    def signature_value(self):
        """Gets the signature_value of this Signature.  # noqa: E501

        Gets or sets an array of bytes representing a signature value as base64 string.  # noqa: E501

        :return: The signature_value of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._signature_value

    @signature_value.setter
    def signature_value(self, signature_value):
        """Sets the signature_value of this Signature.

        Gets or sets an array of bytes representing a signature value as base64 string.  # noqa: E501

        :param signature_value: The signature_value of this Signature.  # noqa: E501
        :type: str
        """
        self._signature_value = signature_value

    @property
    def sign_time(self):
        """Gets the sign_time of this Signature.  # noqa: E501

        Gets or sets the time the document was signed.  # noqa: E501

        :return: The sign_time of this Signature.  # noqa: E501
        :rtype: datetime
        """
        return self._sign_time

    @sign_time.setter
    def sign_time(self, sign_time):
        """Sets the sign_time of this Signature.

        Gets or sets the time the document was signed.  # noqa: E501

        :param sign_time: The sign_time of this Signature.  # noqa: E501
        :type: datetime
        """
        self._sign_time = sign_time

    @property
    def subject_name(self):
        """Gets the subject_name of this Signature.  # noqa: E501

        Gets or sets the subject distinguished name of the certificate that was used to sign the document.  # noqa: E501

        :return: The subject_name of this Signature.  # noqa: E501
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this Signature.

        Gets or sets the subject distinguished name of the certificate that was used to sign the document.  # noqa: E501

        :param subject_name: The subject_name of this Signature.  # noqa: E501
        :type: str
        """
        self._subject_name = subject_name


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._is_valid is None:
            raise ValueError("Property IsValid in Signature is required.")  # noqa: E501
        if self._sign_time is None:
            raise ValueError("Property SignTime in Signature is required.")  # noqa: E501

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
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other