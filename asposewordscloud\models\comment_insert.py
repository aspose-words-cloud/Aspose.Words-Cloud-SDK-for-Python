# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="comment_insert.py">
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

class CommentInsert(object):
    """Comment insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'range_start': 'PositionInsideNode',
        'range_end': 'PositionInsideNode',
        'author': 'str',
        'initial': 'str',
        'date_time': 'datetime',
        'text': 'str'
    }

    attribute_map = {
        'range_start': 'RangeStart',
        'range_end': 'RangeEnd',
        'author': 'Author',
        'initial': 'Initial',
        'date_time': 'DateTime',
        'text': 'Text'
    }

    def __init__(self, range_start=None, range_end=None, author=None, initial=None, date_time=None, text=None):  # noqa: E501
        """CommentInsert - a model defined in Swagger"""  # noqa: E501

        self._range_start = None
        self._range_end = None
        self._author = None
        self._initial = None
        self._date_time = None
        self._text = None
        self.discriminator = None

        if range_start is not None:
            self.range_start = range_start
        if range_end is not None:
            self.range_end = range_end
        if author is not None:
            self.author = author
        if initial is not None:
            self.initial = initial
        if date_time is not None:
            self.date_time = date_time
        if text is not None:
            self.text = text

    @property
    def range_start(self):
        """Gets the range_start of this CommentInsert.  # noqa: E501

        Gets or sets the link to comment range start node.  # noqa: E501

        :return: The range_start of this CommentInsert.  # noqa: E501
        :rtype: PositionInsideNode
        """
        return self._range_start

    @range_start.setter
    def range_start(self, range_start):
        """Sets the range_start of this CommentInsert.

        Gets or sets the link to comment range start node.  # noqa: E501

        :param range_start: The range_start of this CommentInsert.  # noqa: E501
        :type: PositionInsideNode
        """
        self._range_start = range_start

    @property
    def range_end(self):
        """Gets the range_end of this CommentInsert.  # noqa: E501

        Gets or sets the link to comment range end node.  # noqa: E501

        :return: The range_end of this CommentInsert.  # noqa: E501
        :rtype: PositionInsideNode
        """
        return self._range_end

    @range_end.setter
    def range_end(self, range_end):
        """Sets the range_end of this CommentInsert.

        Gets or sets the link to comment range end node.  # noqa: E501

        :param range_end: The range_end of this CommentInsert.  # noqa: E501
        :type: PositionInsideNode
        """
        self._range_end = range_end

    @property
    def author(self):
        """Gets the author of this CommentInsert.  # noqa: E501

        Gets or sets the author name for a comment. Cannot be null.Default is an empty string.  # noqa: E501

        :return: The author of this CommentInsert.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this CommentInsert.

        Gets or sets the author name for a comment. Cannot be null.Default is an empty string.  # noqa: E501

        :param author: The author of this CommentInsert.  # noqa: E501
        :type: str
        """
        self._author = author

    @property
    def initial(self):
        """Gets the initial of this CommentInsert.  # noqa: E501

        Gets or sets the initials of the user associated with a specific comment. Cannot be null.Default is an empty string.  # noqa: E501

        :return: The initial of this CommentInsert.  # noqa: E501
        :rtype: str
        """
        return self._initial

    @initial.setter
    def initial(self, initial):
        """Sets the initial of this CommentInsert.

        Gets or sets the initials of the user associated with a specific comment. Cannot be null.Default is an empty string.  # noqa: E501

        :param initial: The initial of this CommentInsert.  # noqa: E501
        :type: str
        """
        self._initial = initial

    @property
    def date_time(self):
        """Gets the date_time of this CommentInsert.  # noqa: E501

        Gets or sets the date and time that the comment was made. Default is MinValue03.01.0001.  # noqa: E501

        :return: The date_time of this CommentInsert.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this CommentInsert.

        Gets or sets the date and time that the comment was made. Default is MinValue03.01.0001.  # noqa: E501

        :param date_time: The date_time of this CommentInsert.  # noqa: E501
        :type: datetime
        """
        self._date_time = date_time

    @property
    def text(self):
        """Gets the text of this CommentInsert.  # noqa: E501

        Gets or sets text of the comment. This method allows to quickly set text of a comment from a string. The string can contain paragraph breaks, this will create paragraphs of text in the comment accordingly.  # noqa: E501

        :return: The text of this CommentInsert.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CommentInsert.

        Gets or sets text of the comment. This method allows to quickly set text of a comment from a string. The string can contain paragraph breaks, this will create paragraphs of text in the comment accordingly.  # noqa: E501

        :param text: The text of this CommentInsert.  # noqa: E501
        :type: str
        """
        self._text = text


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._range_start is None:
            raise ValueError("Property RangeStart in CommentInsert is required.")  # noqa: E501
        if self._range_end is None:
            raise ValueError("Property RangeEnd in CommentInsert is required.")  # noqa: E501
        if self._author is None:
            raise ValueError("Property Author in CommentInsert is required.")  # noqa: E501
        if self._initial is None:
            raise ValueError("Property Initial in CommentInsert is required.")  # noqa: E501
        if self._text is None:
            raise ValueError("Property Text in CommentInsert is required.")  # noqa: E501

        if self._range_start is not None:
            self._range_start.validate()



        if self._range_end is not None:
            self._range_end.validate()






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
        if not isinstance(other, CommentInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other