# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="optimization_options.py">
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

class OptimizationOptions(object):
    """Container class for the document optimization options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ms_word_version': 'str'
    }

    attribute_map = {
        'ms_word_version': 'MsWordVersion'
    }

    def __init__(self, ms_word_version=None):  # noqa: E501
        """OptimizationOptions - a model defined in Swagger"""  # noqa: E501

        self._ms_word_version = None
        self.discriminator = None

        if ms_word_version is not None:
            self.ms_word_version = ms_word_version

    @property
    def ms_word_version(self):
        """Gets the ms_word_version of this OptimizationOptions.  # noqa: E501

        Gets or sets the specific MSWord version.  # noqa: E501

        :return: The ms_word_version of this OptimizationOptions.  # noqa: E501
        :rtype: str
        """
        return self._ms_word_version

    @ms_word_version.setter
    def ms_word_version(self, ms_word_version):
        """Sets the ms_word_version of this OptimizationOptions.

        Gets or sets the specific MSWord version.  # noqa: E501

        :param ms_word_version: The ms_word_version of this OptimizationOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Word2000", "Word2002", "Word2003", "Word2007", "Word2010", "Word2013", "Word2016", "Word2019"]  # noqa: E501
        if not ms_word_version.isdigit():
            if ms_word_version not in allowed_values:
                raise ValueError(
                    "Invalid value for `ms_word_version` ({0}), must be one of {1}"  # noqa: E501
                    .format(ms_word_version, allowed_values))
            self._ms_word_version = ms_word_version
        else:
            self._ms_word_version = allowed_values[int(ms_word_version) if six.PY3 else long(ms_word_version)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._ms_word_version is None:
            raise ValueError("Property MsWordVersion in OptimizationOptions is required.")  # noqa: E501

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
        if not isinstance(other, OptimizationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other