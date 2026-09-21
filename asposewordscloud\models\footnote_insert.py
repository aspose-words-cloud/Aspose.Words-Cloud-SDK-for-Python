# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="footnote_insert.py">
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

class FootnoteInsert(object):
    """Footnote for insert.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'position': 'Position',
        'footnote_type': 'str',
        'reference_mark': 'str',
        'text': 'str'
    }

    attribute_map = {
        'position': 'Position',
        'footnote_type': 'FootnoteType',
        'reference_mark': 'ReferenceMark',
        'text': 'Text'
    }

    def __init__(self, position=None, footnote_type=None, reference_mark=None, text=None):  # noqa: E501
        """FootnoteInsert - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._footnote_type = None
        self._reference_mark = None
        self._text = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if footnote_type is not None:
            self.footnote_type = footnote_type
        if reference_mark is not None:
            self.reference_mark = reference_mark
        if text is not None:
            self.text = text

    @property
    def position(self):
        """Gets the position of this FootnoteInsert.  # noqa: E501

        Gets or sets the link to range start node.  # noqa: E501

        :return: The position of this FootnoteInsert.  # noqa: E501
        :rtype: Position
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this FootnoteInsert.

        Gets or sets the link to range start node.  # noqa: E501

        :param position: The position of this FootnoteInsert.  # noqa: E501
        :type: Position
        """
        self._position = position

    @property
    def footnote_type(self):
        """Gets the footnote_type of this FootnoteInsert.  # noqa: E501

        Gets or sets the option, that specifies whether this is a footnote or endnote.  # noqa: E501

        :return: The footnote_type of this FootnoteInsert.  # noqa: E501
        :rtype: str
        """
        return self._footnote_type

    @footnote_type.setter
    def footnote_type(self, footnote_type):
        """Sets the footnote_type of this FootnoteInsert.

        Gets or sets the option, that specifies whether this is a footnote or endnote.  # noqa: E501

        :param footnote_type: The footnote_type of this FootnoteInsert.  # noqa: E501
        :type: str
        """
        allowed_values = ["Footnote", "Endnote"]  # noqa: E501
        if not footnote_type.isdigit():
            if footnote_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `footnote_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(footnote_type, allowed_values))
            self._footnote_type = footnote_type
        else:
            self._footnote_type = allowed_values[int(footnote_type) if six.PY3 else long(footnote_type)]

    @property
    def reference_mark(self):
        """Gets the reference_mark of this FootnoteInsert.  # noqa: E501

        Gets or sets the custom reference mark to be used for this footnote. The default value is Empty, meaning auto-numbered footnotes are used. RTF-format can only store 1 symbol as custom reference mark, so upon export only the first symbol will be written others will be discard.  # noqa: E501

        :return: The reference_mark of this FootnoteInsert.  # noqa: E501
        :rtype: str
        """
        return self._reference_mark

    @reference_mark.setter
    def reference_mark(self, reference_mark):
        """Sets the reference_mark of this FootnoteInsert.

        Gets or sets the custom reference mark to be used for this footnote. The default value is Empty, meaning auto-numbered footnotes are used. RTF-format can only store 1 symbol as custom reference mark, so upon export only the first symbol will be written others will be discard.  # noqa: E501

        :param reference_mark: The reference_mark of this FootnoteInsert.  # noqa: E501
        :type: str
        """
        self._reference_mark = reference_mark

    @property
    def text(self):
        """Gets the text of this FootnoteInsert.  # noqa: E501

        Gets or sets text of the footnote. This method allows to quickly set text of a footnote from a string. The string can contain paragraph breaks, this will create paragraphs of text in the footnote accordingly.  # noqa: E501

        :return: The text of this FootnoteInsert.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FootnoteInsert.

        Gets or sets text of the footnote. This method allows to quickly set text of a footnote from a string. The string can contain paragraph breaks, this will create paragraphs of text in the footnote accordingly.  # noqa: E501

        :param text: The text of this FootnoteInsert.  # noqa: E501
        :type: str
        """
        self._text = text


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._position is not None:
            self._position.validate()





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
        if not isinstance(other, FootnoteInsert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other