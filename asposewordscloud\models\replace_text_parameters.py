# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="replace_text_parameters.py">
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

class ReplaceTextParameters(object):
    """Class for document replace text request building.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'apply_superscript': 'bool',
        'is_match_case': 'bool',
        'is_match_whole_word': 'bool',
        'is_old_value_regex': 'bool',
        'new_value': 'str',
        'old_value': 'str'
    }

    attribute_map = {
        'apply_superscript': 'ApplySuperscript',
        'is_match_case': 'IsMatchCase',
        'is_match_whole_word': 'IsMatchWholeWord',
        'is_old_value_regex': 'IsOldValueRegex',
        'new_value': 'NewValue',
        'old_value': 'OldValue'
    }

    def __init__(self, apply_superscript=None, is_match_case=None, is_match_whole_word=None, is_old_value_regex=None, new_value=None, old_value=None):  # noqa: E501
        """ReplaceTextParameters - a model defined in Swagger"""  # noqa: E501

        self._apply_superscript = None
        self._is_match_case = None
        self._is_match_whole_word = None
        self._is_old_value_regex = None
        self._new_value = None
        self._old_value = None
        self.discriminator = None

        if apply_superscript is not None:
            self.apply_superscript = apply_superscript
        if is_match_case is not None:
            self.is_match_case = is_match_case
        if is_match_whole_word is not None:
            self.is_match_whole_word = is_match_whole_word
        if is_old_value_regex is not None:
            self.is_old_value_regex = is_old_value_regex
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value

    @property
    def apply_superscript(self):
        """Gets the apply_superscript of this ReplaceTextParameters.  # noqa: E501

        Gets or sets a value indicating whether apply superscript to font or not.  # noqa: E501

        :return: The apply_superscript of this ReplaceTextParameters.  # noqa: E501
        :rtype: bool
        """
        return self._apply_superscript

    @apply_superscript.setter
    def apply_superscript(self, apply_superscript):
        """Sets the apply_superscript of this ReplaceTextParameters.

        Gets or sets a value indicating whether apply superscript to font or not.  # noqa: E501

        :param apply_superscript: The apply_superscript of this ReplaceTextParameters.  # noqa: E501
        :type: bool
        """
        self._apply_superscript = apply_superscript

    @property
    def is_match_case(self):
        """Gets the is_match_case of this ReplaceTextParameters.  # noqa: E501

        Gets or sets a value indicating whether flag, true means the search is case-sensitive; false means the search is not case-sensitive.  # noqa: E501

        :return: The is_match_case of this ReplaceTextParameters.  # noqa: E501
        :rtype: bool
        """
        return self._is_match_case

    @is_match_case.setter
    def is_match_case(self, is_match_case):
        """Sets the is_match_case of this ReplaceTextParameters.

        Gets or sets a value indicating whether flag, true means the search is case-sensitive; false means the search is not case-sensitive.  # noqa: E501

        :param is_match_case: The is_match_case of this ReplaceTextParameters.  # noqa: E501
        :type: bool
        """
        self._is_match_case = is_match_case

    @property
    def is_match_whole_word(self):
        """Gets the is_match_whole_word of this ReplaceTextParameters.  # noqa: E501

        Gets or sets a value indicating whether flag, means that only whole word matched are replaced.  # noqa: E501

        :return: The is_match_whole_word of this ReplaceTextParameters.  # noqa: E501
        :rtype: bool
        """
        return self._is_match_whole_word

    @is_match_whole_word.setter
    def is_match_whole_word(self, is_match_whole_word):
        """Sets the is_match_whole_word of this ReplaceTextParameters.

        Gets or sets a value indicating whether flag, means that only whole word matched are replaced.  # noqa: E501

        :param is_match_whole_word: The is_match_whole_word of this ReplaceTextParameters.  # noqa: E501
        :type: bool
        """
        self._is_match_whole_word = is_match_whole_word

    @property
    def is_old_value_regex(self):
        """Gets the is_old_value_regex of this ReplaceTextParameters.  # noqa: E501

        Gets or sets a value indicating whether flag, means that OldValue contains regex expression.  # noqa: E501

        :return: The is_old_value_regex of this ReplaceTextParameters.  # noqa: E501
        :rtype: bool
        """
        return self._is_old_value_regex

    @is_old_value_regex.setter
    def is_old_value_regex(self, is_old_value_regex):
        """Sets the is_old_value_regex of this ReplaceTextParameters.

        Gets or sets a value indicating whether flag, means that OldValue contains regex expression.  # noqa: E501

        :param is_old_value_regex: The is_old_value_regex of this ReplaceTextParameters.  # noqa: E501
        :type: bool
        """
        self._is_old_value_regex = is_old_value_regex

    @property
    def new_value(self):
        """Gets the new_value of this ReplaceTextParameters.  # noqa: E501

        Gets or sets the new text value to replace by.  # noqa: E501

        :return: The new_value of this ReplaceTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ReplaceTextParameters.

        Gets or sets the new text value to replace by.  # noqa: E501

        :param new_value: The new_value of this ReplaceTextParameters.  # noqa: E501
        :type: str
        """
        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this ReplaceTextParameters.  # noqa: E501

        Gets or sets the old text value (or regex pattern IsOldValueRegex) to replace.  # noqa: E501

        :return: The old_value of this ReplaceTextParameters.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ReplaceTextParameters.

        Gets or sets the old text value (or regex pattern IsOldValueRegex) to replace.  # noqa: E501

        :param old_value: The old_value of this ReplaceTextParameters.  # noqa: E501
        :type: str
        """
        self._old_value = old_value


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._is_match_case is None:
            raise ValueError("Property IsMatchCase in ReplaceTextParameters is required.")  # noqa: E501
        if self._is_match_whole_word is None:
            raise ValueError("Property IsMatchWholeWord in ReplaceTextParameters is required.")  # noqa: E501
        if self._is_old_value_regex is None:
            raise ValueError("Property IsOldValueRegex in ReplaceTextParameters is required.")  # noqa: E501
        if self._new_value is None:
            raise ValueError("Property NewValue in ReplaceTextParameters is required.")  # noqa: E501
        if self._old_value is None:
            raise ValueError("Property OldValue in ReplaceTextParameters is required.")  # noqa: E501

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
        if not isinstance(other, ReplaceTextParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other