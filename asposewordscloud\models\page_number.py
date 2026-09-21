# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="page_number.py">
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

class PageNumber(object):
    """Class is used for insert page number request building.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alignment': 'str',
        'format': 'str',
        'is_top': 'bool',
        'page_starting_number': 'int',
        'set_page_number_on_first_page': 'bool'
    }

    attribute_map = {
        'alignment': 'Alignment',
        'format': 'Format',
        'is_top': 'IsTop',
        'page_starting_number': 'PageStartingNumber',
        'set_page_number_on_first_page': 'SetPageNumberOnFirstPage'
    }

    def __init__(self, alignment=None, format=None, is_top=None, page_starting_number=None, set_page_number_on_first_page=None):  # noqa: E501
        """PageNumber - a model defined in Swagger"""  # noqa: E501

        self._alignment = None
        self._format = None
        self._is_top = None
        self._page_starting_number = None
        self._set_page_number_on_first_page = None
        self.discriminator = None

        if alignment is not None:
            self.alignment = alignment
        if format is not None:
            self.format = format
        if is_top is not None:
            self.is_top = is_top
        if page_starting_number is not None:
            self.page_starting_number = page_starting_number
        if set_page_number_on_first_page is not None:
            self.set_page_number_on_first_page = set_page_number_on_first_page

    @property
    def alignment(self):
        """Gets the alignment of this PageNumber.  # noqa: E501

        Gets or sets text alignment, possible values are left, right, center or justify.  # noqa: E501

        :return: The alignment of this PageNumber.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this PageNumber.

        Gets or sets text alignment, possible values are left, right, center or justify.  # noqa: E501

        :param alignment: The alignment of this PageNumber.  # noqa: E501
        :type: str
        """
        self._alignment = alignment

    @property
    def format(self):
        """Gets the format of this PageNumber.  # noqa: E501

        Gets or sets the page number format, e.g. "{PAGE} of {NUMPAGES}".  # noqa: E501

        :return: The format of this PageNumber.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PageNumber.

        Gets or sets the page number format, e.g. "{PAGE} of {NUMPAGES}".  # noqa: E501

        :param format: The format of this PageNumber.  # noqa: E501
        :type: str
        """
        self._format = format

    @property
    def is_top(self):
        """Gets the is_top of this PageNumber.  # noqa: E501

        Gets or sets a value indicating whether if true the page number is added at the top of the page, else at the bottom.  # noqa: E501

        :return: The is_top of this PageNumber.  # noqa: E501
        :rtype: bool
        """
        return self._is_top

    @is_top.setter
    def is_top(self, is_top):
        """Sets the is_top of this PageNumber.

        Gets or sets a value indicating whether if true the page number is added at the top of the page, else at the bottom.  # noqa: E501

        :param is_top: The is_top of this PageNumber.  # noqa: E501
        :type: bool
        """
        self._is_top = is_top

    @property
    def page_starting_number(self):
        """Gets the page_starting_number of this PageNumber.  # noqa: E501

        Gets or sets the starting page number of the document.  # noqa: E501

        :return: The page_starting_number of this PageNumber.  # noqa: E501
        :rtype: int
        """
        return self._page_starting_number

    @page_starting_number.setter
    def page_starting_number(self, page_starting_number):
        """Sets the page_starting_number of this PageNumber.

        Gets or sets the starting page number of the document.  # noqa: E501

        :param page_starting_number: The page_starting_number of this PageNumber.  # noqa: E501
        :type: int
        """
        self._page_starting_number = page_starting_number

    @property
    def set_page_number_on_first_page(self):
        """Gets the set_page_number_on_first_page of this PageNumber.  # noqa: E501

        Gets or sets a value indicating whether if true the page number is added on first page too.  # noqa: E501

        :return: The set_page_number_on_first_page of this PageNumber.  # noqa: E501
        :rtype: bool
        """
        return self._set_page_number_on_first_page

    @set_page_number_on_first_page.setter
    def set_page_number_on_first_page(self, set_page_number_on_first_page):
        """Sets the set_page_number_on_first_page of this PageNumber.

        Gets or sets a value indicating whether if true the page number is added on first page too.  # noqa: E501

        :param set_page_number_on_first_page: The set_page_number_on_first_page of this PageNumber.  # noqa: E501
        :type: bool
        """
        self._set_page_number_on_first_page = set_page_number_on_first_page


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._is_top is None:
            raise ValueError("Property IsTop in PageNumber is required.")  # noqa: E501
        if self._set_page_number_on_first_page is None:
            raise ValueError("Property SetPageNumberOnFirstPage in PageNumber is required.")  # noqa: E501

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
        if not isinstance(other, PageNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other