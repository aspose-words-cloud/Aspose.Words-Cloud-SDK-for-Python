# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="split_document_result.py">
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

class SplitDocumentResult(object):
    """Result of splitting document.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_document': 'FileLink',
        'zipped_pages': 'FileLink',
        'pages': 'list[FileLink]'
    }

    attribute_map = {
        'source_document': 'SourceDocument',
        'zipped_pages': 'ZippedPages',
        'pages': 'Pages'
    }

    def __init__(self, source_document=None, zipped_pages=None, pages=None):  # noqa: E501
        """SplitDocumentResult - a model defined in Swagger"""  # noqa: E501

        self._source_document = None
        self._zipped_pages = None
        self._pages = None
        self.discriminator = None

        if source_document is not None:
            self.source_document = source_document
        if zipped_pages is not None:
            self.zipped_pages = zipped_pages
        if pages is not None:
            self.pages = pages

    @property
    def source_document(self):
        """Gets the source_document of this SplitDocumentResult.  # noqa: E501

        Gets or sets the link to the source document.  # noqa: E501

        :return: The source_document of this SplitDocumentResult.  # noqa: E501
        :rtype: FileLink
        """
        return self._source_document

    @source_document.setter
    def source_document(self, source_document):
        """Sets the source_document of this SplitDocumentResult.

        Gets or sets the link to the source document.  # noqa: E501

        :param source_document: The source_document of this SplitDocumentResult.  # noqa: E501
        :type: FileLink
        """
        self._source_document = source_document

    @property
    def zipped_pages(self):
        """Gets the zipped_pages of this SplitDocumentResult.  # noqa: E501

        Gets or sets the link to the file archive with pages.  # noqa: E501

        :return: The zipped_pages of this SplitDocumentResult.  # noqa: E501
        :rtype: FileLink
        """
        return self._zipped_pages

    @zipped_pages.setter
    def zipped_pages(self, zipped_pages):
        """Sets the zipped_pages of this SplitDocumentResult.

        Gets or sets the link to the file archive with pages.  # noqa: E501

        :param zipped_pages: The zipped_pages of this SplitDocumentResult.  # noqa: E501
        :type: FileLink
        """
        self._zipped_pages = zipped_pages

    @property
    def pages(self):
        """Gets the pages of this SplitDocumentResult.  # noqa: E501

        Gets or sets the list of pages.  # noqa: E501

        :return: The pages of this SplitDocumentResult.  # noqa: E501
        :rtype: list[FileLink]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this SplitDocumentResult.

        Gets or sets the list of pages.  # noqa: E501

        :param pages: The pages of this SplitDocumentResult.  # noqa: E501
        :type: list[FileLink]
        """
        self._pages = pages


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._source_document is not None:
            self._source_document.validate()



        if self._zipped_pages is not None:
            self._zipped_pages.validate()



        if self._pages is not None:
            for elementPages in self._pages:
                if elementPages is not None:
                    elementPages.validate()


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
        if not isinstance(other, SplitDocumentResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other