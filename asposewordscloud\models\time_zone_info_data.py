# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="time_zone_info_data.py">
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

class TimeZoneInfoData(object):
    """Class to specify TimeZoneInfo parameters.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base_utc_offset': 'str',
        'display_name': 'str',
        'id': 'str',
        'standard_display_name': 'str'
    }

    attribute_map = {
        'base_utc_offset': 'BaseUtcOffset',
        'display_name': 'DisplayName',
        'id': 'Id',
        'standard_display_name': 'StandardDisplayName'
    }

    def __init__(self, base_utc_offset=None, display_name=None, id=None, standard_display_name=None):  # noqa: E501
        """TimeZoneInfoData - a model defined in Swagger"""  # noqa: E501

        self._base_utc_offset = None
        self._display_name = None
        self._id = None
        self._standard_display_name = None
        self.discriminator = None

        if base_utc_offset is not None:
            self.base_utc_offset = base_utc_offset
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if standard_display_name is not None:
            self.standard_display_name = standard_display_name

    @property
    def base_utc_offset(self):
        """Gets the base_utc_offset of this TimeZoneInfoData.  # noqa: E501

        Gets or sets base utc offset in hh:mm:ss format.  # noqa: E501

        :return: The base_utc_offset of this TimeZoneInfoData.  # noqa: E501
        :rtype: str
        """
        return self._base_utc_offset

    @base_utc_offset.setter
    def base_utc_offset(self, base_utc_offset):
        """Sets the base_utc_offset of this TimeZoneInfoData.

        Gets or sets base utc offset in hh:mm:ss format.  # noqa: E501

        :param base_utc_offset: The base_utc_offset of this TimeZoneInfoData.  # noqa: E501
        :type: str
        """
        self._base_utc_offset = base_utc_offset

    @property
    def display_name(self):
        """Gets the display_name of this TimeZoneInfoData.  # noqa: E501

        Gets or sets display name.  # noqa: E501

        :return: The display_name of this TimeZoneInfoData.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TimeZoneInfoData.

        Gets or sets display name.  # noqa: E501

        :param display_name: The display_name of this TimeZoneInfoData.  # noqa: E501
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this TimeZoneInfoData.  # noqa: E501

        Gets or sets an Id string for CustomTimeZoneInfo.  # noqa: E501

        :return: The id of this TimeZoneInfoData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeZoneInfoData.

        Gets or sets an Id string for CustomTimeZoneInfo.  # noqa: E501

        :param id: The id of this TimeZoneInfoData.  # noqa: E501
        :type: str
        """
        self._id = id

    @property
    def standard_display_name(self):
        """Gets the standard_display_name of this TimeZoneInfoData.  # noqa: E501

        Gets or sets standard display name.  # noqa: E501

        :return: The standard_display_name of this TimeZoneInfoData.  # noqa: E501
        :rtype: str
        """
        return self._standard_display_name

    @standard_display_name.setter
    def standard_display_name(self, standard_display_name):
        """Sets the standard_display_name of this TimeZoneInfoData.

        Gets or sets standard display name.  # noqa: E501

        :param standard_display_name: The standard_display_name of this TimeZoneInfoData.  # noqa: E501
        :type: str
        """
        self._standard_display_name = standard_display_name


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

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
        if not isinstance(other, TimeZoneInfoData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other