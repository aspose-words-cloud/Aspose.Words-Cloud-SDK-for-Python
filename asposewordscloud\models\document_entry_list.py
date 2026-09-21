# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="document_entry_list.py">
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

class DocumentEntryList(object):
    """Represents a list of documents which will be appended to the original resource document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'append_all_entries_to_one_section': 'bool',
        'apply_base_document_headers_and_footers_to_appending_documents': 'bool',
        'document_entries': 'list[DocumentEntry]'
    }

    attribute_map = {
        'append_all_entries_to_one_section': 'AppendAllEntriesToOneSection',
        'apply_base_document_headers_and_footers_to_appending_documents': 'ApplyBaseDocumentHeadersAndFootersToAppendingDocuments',
        'document_entries': 'DocumentEntries'
    }

    def __init__(self, append_all_entries_to_one_section=None, apply_base_document_headers_and_footers_to_appending_documents=None, document_entries=None):  # noqa: E501
        """DocumentEntryList - a model defined in Swagger"""  # noqa: E501

        self._append_all_entries_to_one_section = None
        self._apply_base_document_headers_and_footers_to_appending_documents = None
        self._document_entries = None
        self.discriminator = None

        if append_all_entries_to_one_section is not None:
            self.append_all_entries_to_one_section = append_all_entries_to_one_section
        if apply_base_document_headers_and_footers_to_appending_documents is not None:
            self.apply_base_document_headers_and_footers_to_appending_documents = apply_base_document_headers_and_footers_to_appending_documents
        if document_entries is not None:
            self.document_entries = document_entries

    @property
    def append_all_entries_to_one_section(self):
        """Gets the append_all_entries_to_one_section of this DocumentEntryList.  # noqa: E501

        Gets or sets a value indicating whether to append all documents to the same section.  # noqa: E501

        :return: The append_all_entries_to_one_section of this DocumentEntryList.  # noqa: E501
        :rtype: bool
        """
        return self._append_all_entries_to_one_section

    @append_all_entries_to_one_section.setter
    def append_all_entries_to_one_section(self, append_all_entries_to_one_section):
        """Sets the append_all_entries_to_one_section of this DocumentEntryList.

        Gets or sets a value indicating whether to append all documents to the same section.  # noqa: E501

        :param append_all_entries_to_one_section: The append_all_entries_to_one_section of this DocumentEntryList.  # noqa: E501
        :type: bool
        """
        self._append_all_entries_to_one_section = append_all_entries_to_one_section

    @property
    def apply_base_document_headers_and_footers_to_appending_documents(self):
        """Gets the apply_base_document_headers_and_footers_to_appending_documents of this DocumentEntryList.  # noqa: E501

        Gets or sets a value indicating whether to apply headers and footers from base document to appending documents. The default value is true.  # noqa: E501

        :return: The apply_base_document_headers_and_footers_to_appending_documents of this DocumentEntryList.  # noqa: E501
        :rtype: bool
        """
        return self._apply_base_document_headers_and_footers_to_appending_documents

    @apply_base_document_headers_and_footers_to_appending_documents.setter
    def apply_base_document_headers_and_footers_to_appending_documents(self, apply_base_document_headers_and_footers_to_appending_documents):
        """Sets the apply_base_document_headers_and_footers_to_appending_documents of this DocumentEntryList.

        Gets or sets a value indicating whether to apply headers and footers from base document to appending documents. The default value is true.  # noqa: E501

        :param apply_base_document_headers_and_footers_to_appending_documents: The apply_base_document_headers_and_footers_to_appending_documents of this DocumentEntryList.  # noqa: E501
        :type: bool
        """
        self._apply_base_document_headers_and_footers_to_appending_documents = apply_base_document_headers_and_footers_to_appending_documents

    @property
    def document_entries(self):
        """Gets the document_entries of this DocumentEntryList.  # noqa: E501

        Gets or sets the list of documents.  # noqa: E501

        :return: The document_entries of this DocumentEntryList.  # noqa: E501
        :rtype: list[DocumentEntry]
        """
        return self._document_entries

    @document_entries.setter
    def document_entries(self, document_entries):
        """Sets the document_entries of this DocumentEntryList.

        Gets or sets the list of documents.  # noqa: E501

        :param document_entries: The document_entries of this DocumentEntryList.  # noqa: E501
        :type: list[DocumentEntry]
        """
        self._document_entries = document_entries


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""
        if self._document_entries is not None:
            for element in self._document_entries:
                element.extract_files_content(filesContentResult)


    def validate(self):
        """Validate all required properties in model"""
        if self._document_entries is None:
            raise ValueError("Property DocumentEntries in DocumentEntryList is required.")  # noqa: E501

        if self._document_entries is not None:
            for elementDocumentEntries in self._document_entries:
                if elementDocumentEntries is not None:
                    elementDocumentEntries.validate()


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
        if not isinstance(other, DocumentEntryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other