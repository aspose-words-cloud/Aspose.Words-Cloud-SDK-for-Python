# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="document_stat_data.py">
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

class DocumentStatData(object):
    """Container for the document's statistical data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'footnotes_stat_data': 'FootnotesStatData',
        'page_count': 'int',
        'paragraph_count': 'int',
        'word_count': 'int',
        'page_stat_data': 'list[PageStatData]'
    }

    attribute_map = {
        'footnotes_stat_data': 'FootnotesStatData',
        'page_count': 'PageCount',
        'paragraph_count': 'ParagraphCount',
        'word_count': 'WordCount',
        'page_stat_data': 'PageStatData'
    }

    def __init__(self, footnotes_stat_data=None, page_count=None, paragraph_count=None, word_count=None, page_stat_data=None):  # noqa: E501
        """DocumentStatData - a model defined in Swagger"""  # noqa: E501

        self._footnotes_stat_data = None
        self._page_count = None
        self._paragraph_count = None
        self._word_count = None
        self._page_stat_data = None
        self.discriminator = None

        if footnotes_stat_data is not None:
            self.footnotes_stat_data = footnotes_stat_data
        if page_count is not None:
            self.page_count = page_count
        if paragraph_count is not None:
            self.paragraph_count = paragraph_count
        if word_count is not None:
            self.word_count = word_count
        if page_stat_data is not None:
            self.page_stat_data = page_stat_data

    @property
    def footnotes_stat_data(self):
        """Gets the footnotes_stat_data of this DocumentStatData.  # noqa: E501

        Gets or sets the detailed statistics on footnotes.  # noqa: E501

        :return: The footnotes_stat_data of this DocumentStatData.  # noqa: E501
        :rtype: FootnotesStatData
        """
        return self._footnotes_stat_data

    @footnotes_stat_data.setter
    def footnotes_stat_data(self, footnotes_stat_data):
        """Sets the footnotes_stat_data of this DocumentStatData.

        Gets or sets the detailed statistics on footnotes.  # noqa: E501

        :param footnotes_stat_data: The footnotes_stat_data of this DocumentStatData.  # noqa: E501
        :type: FootnotesStatData
        """
        self._footnotes_stat_data = footnotes_stat_data

    @property
    def page_count(self):
        """Gets the page_count of this DocumentStatData.  # noqa: E501

        Gets or sets the total count of pages in the document.  # noqa: E501

        :return: The page_count of this DocumentStatData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this DocumentStatData.

        Gets or sets the total count of pages in the document.  # noqa: E501

        :param page_count: The page_count of this DocumentStatData.  # noqa: E501
        :type: int
        """
        self._page_count = page_count

    @property
    def paragraph_count(self):
        """Gets the paragraph_count of this DocumentStatData.  # noqa: E501

        Gets or sets the total count of paragraphs in the document.  # noqa: E501

        :return: The paragraph_count of this DocumentStatData.  # noqa: E501
        :rtype: int
        """
        return self._paragraph_count

    @paragraph_count.setter
    def paragraph_count(self, paragraph_count):
        """Sets the paragraph_count of this DocumentStatData.

        Gets or sets the total count of paragraphs in the document.  # noqa: E501

        :param paragraph_count: The paragraph_count of this DocumentStatData.  # noqa: E501
        :type: int
        """
        self._paragraph_count = paragraph_count

    @property
    def word_count(self):
        """Gets the word_count of this DocumentStatData.  # noqa: E501

        Gets or sets the total count of words in the document.  # noqa: E501

        :return: The word_count of this DocumentStatData.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this DocumentStatData.

        Gets or sets the total count of words in the document.  # noqa: E501

        :param word_count: The word_count of this DocumentStatData.  # noqa: E501
        :type: int
        """
        self._word_count = word_count

    @property
    def page_stat_data(self):
        """Gets the page_stat_data of this DocumentStatData.  # noqa: E501

        Gets or sets the detailed statistics on all pages.  # noqa: E501

        :return: The page_stat_data of this DocumentStatData.  # noqa: E501
        :rtype: list[PageStatData]
        """
        return self._page_stat_data

    @page_stat_data.setter
    def page_stat_data(self, page_stat_data):
        """Sets the page_stat_data of this DocumentStatData.

        Gets or sets the detailed statistics on all pages.  # noqa: E501

        :param page_stat_data: The page_stat_data of this DocumentStatData.  # noqa: E501
        :type: list[PageStatData]
        """
        self._page_stat_data = page_stat_data


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._page_count is None:
            raise ValueError("Property PageCount in DocumentStatData is required.")  # noqa: E501
        if self._paragraph_count is None:
            raise ValueError("Property ParagraphCount in DocumentStatData is required.")  # noqa: E501
        if self._word_count is None:
            raise ValueError("Property WordCount in DocumentStatData is required.")  # noqa: E501

        if self._footnotes_stat_data is not None:
            self._footnotes_stat_data.validate()






        if self._page_stat_data is not None:
            for elementPageStatData in self._page_stat_data:
                if elementPageStatData is not None:
                    elementPageStatData.validate()


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
        if not isinstance(other, DocumentStatData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other