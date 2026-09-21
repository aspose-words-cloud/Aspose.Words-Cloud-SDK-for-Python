# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="digital_signature_details.py">
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

class DigitalSignatureDetails(object):
    """Container class for details of digital signature.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate_filename': 'str',
        'sign_options': 'SignOptions'
    }

    attribute_map = {
        'certificate_filename': 'CertificateFilename',
        'sign_options': 'SignOptions'
    }

    def __init__(self, certificate_filename=None, sign_options=None):  # noqa: E501
        """DigitalSignatureDetails - a model defined in Swagger"""  # noqa: E501

        self._certificate_filename = None
        self._sign_options = None
        self.discriminator = None

        if certificate_filename is not None:
            self.certificate_filename = certificate_filename
        if sign_options is not None:
            self.sign_options = sign_options

    @property
    def certificate_filename(self):
        """Gets the certificate_filename of this DigitalSignatureDetails.  # noqa: E501

        Gets or sets the certificate's filename using for signing.  # noqa: E501

        :return: The certificate_filename of this DigitalSignatureDetails.  # noqa: E501
        :rtype: str
        """
        return self._certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, certificate_filename):
        """Sets the certificate_filename of this DigitalSignatureDetails.

        Gets or sets the certificate's filename using for signing.  # noqa: E501

        :param certificate_filename: The certificate_filename of this DigitalSignatureDetails.  # noqa: E501
        :type: str
        """
        self._certificate_filename = certificate_filename

    @property
    def sign_options(self):
        """Gets the sign_options of this DigitalSignatureDetails.  # noqa: E501

        Gets or sets signing options.  # noqa: E501

        :return: The sign_options of this DigitalSignatureDetails.  # noqa: E501
        :rtype: SignOptions
        """
        return self._sign_options

    @sign_options.setter
    def sign_options(self, sign_options):
        """Sets the sign_options of this DigitalSignatureDetails.

        Gets or sets signing options.  # noqa: E501

        :param sign_options: The sign_options of this DigitalSignatureDetails.  # noqa: E501
        :type: SignOptions
        """
        self._sign_options = sign_options


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._sign_options is not None:
            self._sign_options.validate()


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
        if not isinstance(other, DigitalSignatureDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other