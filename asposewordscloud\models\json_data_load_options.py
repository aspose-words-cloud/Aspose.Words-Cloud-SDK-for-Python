# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="json_data_load_options.py">
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

class JsonDataLoadOptions(object):
    """Represents options for parsing JSON data. An instance of this class can be passed into constructors of Aspose.Words.Reporting.JsonDataSource.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'always_generate_root_object': 'bool',
        'exact_date_time_parse_formats': 'list[str]',
        'simple_value_parse_mode': 'str'
    }

    attribute_map = {
        'always_generate_root_object': 'AlwaysGenerateRootObject',
        'exact_date_time_parse_formats': 'ExactDateTimeParseFormats',
        'simple_value_parse_mode': 'SimpleValueParseMode'
    }

    def __init__(self, always_generate_root_object=None, exact_date_time_parse_formats=None, simple_value_parse_mode=None):  # noqa: E501
        """JsonDataLoadOptions - a model defined in Swagger"""  # noqa: E501

        self._always_generate_root_object = None
        self._exact_date_time_parse_formats = None
        self._simple_value_parse_mode = None
        self.discriminator = None

        if always_generate_root_object is not None:
            self.always_generate_root_object = always_generate_root_object
        if exact_date_time_parse_formats is not None:
            self.exact_date_time_parse_formats = exact_date_time_parse_formats
        if simple_value_parse_mode is not None:
            self.simple_value_parse_mode = simple_value_parse_mode

    @property
    def always_generate_root_object(self):
        """Gets the always_generate_root_object of this JsonDataLoadOptions.  # noqa: E501

        Gets or sets a value indicating whether a generated data source will always contain an object for a JSON root element. If a JSON root element contains a single complex property, such an object is not created by default. The default value is false.  # noqa: E501

        :return: The always_generate_root_object of this JsonDataLoadOptions.  # noqa: E501
        :rtype: bool
        """
        return self._always_generate_root_object

    @always_generate_root_object.setter
    def always_generate_root_object(self, always_generate_root_object):
        """Sets the always_generate_root_object of this JsonDataLoadOptions.

        Gets or sets a value indicating whether a generated data source will always contain an object for a JSON root element. If a JSON root element contains a single complex property, such an object is not created by default. The default value is false.  # noqa: E501

        :param always_generate_root_object: The always_generate_root_object of this JsonDataLoadOptions.  # noqa: E501
        :type: bool
        """
        self._always_generate_root_object = always_generate_root_object

    @property
    def exact_date_time_parse_formats(self):
        """Gets the exact_date_time_parse_formats of this JsonDataLoadOptions.  # noqa: E501

        Gets or sets exact formats for parsing JSON date-time values while loading JSON. The default is null. Strings encoded using Microsoft® JSON date-time format (for example, "/Date(1224043200000)/") are always recognized as date-time values regardless of a value of this property. The property defines additional formats to be used while parsing date-time values from strings in the following way: • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats is null, the ISO-8601 format and all date-time formats supported for the current, English USA, and English New Zealand cultures are used additionally in the mentioned order. • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats contains strings, they are used as additional date-time formats utilizing the current culture. • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats is empty, no additional date-time formats are used.  # noqa: E501

        :return: The exact_date_time_parse_formats of this JsonDataLoadOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_date_time_parse_formats

    @exact_date_time_parse_formats.setter
    def exact_date_time_parse_formats(self, exact_date_time_parse_formats):
        """Sets the exact_date_time_parse_formats of this JsonDataLoadOptions.

        Gets or sets exact formats for parsing JSON date-time values while loading JSON. The default is null. Strings encoded using Microsoft® JSON date-time format (for example, "/Date(1224043200000)/") are always recognized as date-time values regardless of a value of this property. The property defines additional formats to be used while parsing date-time values from strings in the following way: • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats is null, the ISO-8601 format and all date-time formats supported for the current, English USA, and English New Zealand cultures are used additionally in the mentioned order. • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats contains strings, they are used as additional date-time formats utilizing the current culture. • When Aspose.Words.Reporting.JsonDataLoadOptions.ExactDateTimeParseFormats is empty, no additional date-time formats are used.  # noqa: E501

        :param exact_date_time_parse_formats: The exact_date_time_parse_formats of this JsonDataLoadOptions.  # noqa: E501
        :type: list[str]
        """
        self._exact_date_time_parse_formats = exact_date_time_parse_formats

    @property
    def simple_value_parse_mode(self):
        """Gets the simple_value_parse_mode of this JsonDataLoadOptions.  # noqa: E501

        Gets or sets a mode for parsing JSON simple values (null, boolean, number, integer, and string) while loading JSON. Such a mode does not affect parsing of date-time values. The default is Aspose.Words.Reporting.JsonSimpleValueParseMode.Loose.  # noqa: E501

        :return: The simple_value_parse_mode of this JsonDataLoadOptions.  # noqa: E501
        :rtype: str
        """
        return self._simple_value_parse_mode

    @simple_value_parse_mode.setter
    def simple_value_parse_mode(self, simple_value_parse_mode):
        """Sets the simple_value_parse_mode of this JsonDataLoadOptions.

        Gets or sets a mode for parsing JSON simple values (null, boolean, number, integer, and string) while loading JSON. Such a mode does not affect parsing of date-time values. The default is Aspose.Words.Reporting.JsonSimpleValueParseMode.Loose.  # noqa: E501

        :param simple_value_parse_mode: The simple_value_parse_mode of this JsonDataLoadOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Loose", "Strict"]  # noqa: E501
        if not simple_value_parse_mode.isdigit():
            if simple_value_parse_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `simple_value_parse_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(simple_value_parse_mode, allowed_values))
            self._simple_value_parse_mode = simple_value_parse_mode
        else:
            self._simple_value_parse_mode = allowed_values[int(simple_value_parse_mode) if six.PY3 else long(simple_value_parse_mode)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._always_generate_root_object is None:
            raise ValueError("Property AlwaysGenerateRootObject in JsonDataLoadOptions is required.")  # noqa: E501
        if self._simple_value_parse_mode is None:
            raise ValueError("Property SimpleValueParseMode in JsonDataLoadOptions is required.")  # noqa: E501

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
        if not isinstance(other, JsonDataLoadOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other