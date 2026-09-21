# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="document.py">
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

class Document(object):
    """Represents Words document DTO.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[Link]',
        'document_properties': 'DocumentProperties',
        'file_name': 'str',
        'file_size': 'int',
        'is_encrypted': 'bool',
        'is_signed': 'bool',
        'source_format': 'str'
    }

    attribute_map = {
        'links': 'Links',
        'document_properties': 'DocumentProperties',
        'file_name': 'FileName',
        'file_size': 'FileSize',
        'is_encrypted': 'IsEncrypted',
        'is_signed': 'IsSigned',
        'source_format': 'SourceFormat'
    }

    def __init__(self, links=None, document_properties=None, file_name=None, file_size=None, is_encrypted=None, is_signed=None, source_format=None):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._document_properties = None
        self._file_name = None
        self._file_size = None
        self._is_encrypted = None
        self._is_signed = None
        self._source_format = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if document_properties is not None:
            self.document_properties = document_properties
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if is_encrypted is not None:
            self.is_encrypted = is_encrypted
        if is_signed is not None:
            self.is_signed = is_signed
        if source_format is not None:
            self.source_format = source_format

    @property
    def links(self):
        """Gets the links of this Document.  # noqa: E501

        Gets or sets the list of links that originate from this document.  # noqa: E501

        :return: The links of this Document.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Document.

        Gets or sets the list of links that originate from this document.  # noqa: E501

        :param links: The links of this Document.  # noqa: E501
        :type: list[Link]
        """
        self._links = links

    @property
    def document_properties(self):
        """Gets the document_properties of this Document.  # noqa: E501

        Gets or sets the document properties.  # noqa: E501

        :return: The document_properties of this Document.  # noqa: E501
        :rtype: DocumentProperties
        """
        return self._document_properties

    @document_properties.setter
    def document_properties(self, document_properties):
        """Sets the document_properties of this Document.

        Gets or sets the document properties.  # noqa: E501

        :param document_properties: The document_properties of this Document.  # noqa: E501
        :type: DocumentProperties
        """
        self._document_properties = document_properties

    @property
    def file_name(self):
        """Gets the file_name of this Document.  # noqa: E501

        Gets or sets the name of the file.  # noqa: E501

        :return: The file_name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Document.

        Gets or sets the name of the file.  # noqa: E501

        :param file_name: The file_name of this Document.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this Document.  # noqa: E501

        Gets or sets the file size.  # noqa: E501

        :return: The file_size of this Document.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this Document.

        Gets or sets the file size.  # noqa: E501

        :param file_size: The file_size of this Document.  # noqa: E501
        :type: int
        """
        self._file_size = file_size

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this Document.  # noqa: E501

        Gets or sets a value indicating whether the document is encrypted and requires a password to open.  # noqa: E501

        :return: The is_encrypted of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this Document.

        Gets or sets a value indicating whether the document is encrypted and requires a password to open.  # noqa: E501

        :param is_encrypted: The is_encrypted of this Document.  # noqa: E501
        :type: bool
        """
        self._is_encrypted = is_encrypted

    @property
    def is_signed(self):
        """Gets the is_signed of this Document.  # noqa: E501

        Gets or sets a value indicating whether the document contains a digital signature. This property merely informs that a digital signature is present on a document, but it does not specify whether the signature is valid or not.  # noqa: E501

        :return: The is_signed of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._is_signed

    @is_signed.setter
    def is_signed(self, is_signed):
        """Sets the is_signed of this Document.

        Gets or sets a value indicating whether the document contains a digital signature. This property merely informs that a digital signature is present on a document, but it does not specify whether the signature is valid or not.  # noqa: E501

        :param is_signed: The is_signed of this Document.  # noqa: E501
        :type: bool
        """
        self._is_signed = is_signed

    @property
    def source_format(self):
        """Gets the source_format of this Document.  # noqa: E501

        Gets or sets the original format of the document.  # noqa: E501

        :return: The source_format of this Document.  # noqa: E501
        :rtype: str
        """
        return self._source_format

    @source_format.setter
    def source_format(self, source_format):
        """Sets the source_format of this Document.

        Gets or sets the original format of the document.  # noqa: E501

        :param source_format: The source_format of this Document.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Doc", "Dot", "DocPreWord60", "Docx", "Docm", "Dotx", "Dotm", "FlatOpc", "Rtf", "WordML", "Html", "Mhtml", "Epub", "Text", "Odt", "Ott", "Pdf", "Xps", "Tiff", "Svg", "Azw3"]  # noqa: E501
        if not source_format.isdigit():
            if source_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `source_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(source_format, allowed_values))
            self._source_format = source_format
        else:
            self._source_format = allowed_values[int(source_format) if six.PY3 else long(source_format)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._is_encrypted is None:
            raise ValueError("Property IsEncrypted in Document is required.")  # noqa: E501
        if self._is_signed is None:
            raise ValueError("Property IsSigned in Document is required.")  # noqa: E501
        if self._source_format is None:
            raise ValueError("Property SourceFormat in Document is required.")  # noqa: E501

        if self._links is not None:
            for elementLinks in self._links:
                if elementLinks is not None:
                    elementLinks.validate()



        if self._document_properties is not None:
            self._document_properties.validate()







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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other