# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="font_info.py">
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

class FontInfo(object):
    """DTO container with font info.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_path': 'str',
        'font_family_name': 'str',
        'full_font_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'file_path': 'FilePath',
        'font_family_name': 'FontFamilyName',
        'full_font_name': 'FullFontName',
        'version': 'Version'
    }

    def __init__(self, file_path=None, font_family_name=None, full_font_name=None, version=None):  # noqa: E501
        """FontInfo - a model defined in Swagger"""  # noqa: E501

        self._file_path = None
        self._font_family_name = None
        self._full_font_name = None
        self._version = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if font_family_name is not None:
            self.font_family_name = font_family_name
        if full_font_name is not None:
            self.full_font_name = full_font_name
        if version is not None:
            self.version = version

    @property
    def file_path(self):
        """Gets the file_path of this FontInfo.  # noqa: E501

        Gets or sets the path to the font file if any.  # noqa: E501

        :return: The file_path of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this FontInfo.

        Gets or sets the path to the font file if any.  # noqa: E501

        :param file_path: The file_path of this FontInfo.  # noqa: E501
        :type: str
        """
        self._file_path = file_path

    @property
    def font_family_name(self):
        """Gets the font_family_name of this FontInfo.  # noqa: E501

        Gets or sets the family name of the font.  # noqa: E501

        :return: The font_family_name of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._font_family_name

    @font_family_name.setter
    def font_family_name(self, font_family_name):
        """Sets the font_family_name of this FontInfo.

        Gets or sets the family name of the font.  # noqa: E501

        :param font_family_name: The font_family_name of this FontInfo.  # noqa: E501
        :type: str
        """
        self._font_family_name = font_family_name

    @property
    def full_font_name(self):
        """Gets the full_font_name of this FontInfo.  # noqa: E501

        Gets or sets the full name of the font.  # noqa: E501

        :return: The full_font_name of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._full_font_name

    @full_font_name.setter
    def full_font_name(self, full_font_name):
        """Sets the full_font_name of this FontInfo.

        Gets or sets the full name of the font.  # noqa: E501

        :param full_font_name: The full_font_name of this FontInfo.  # noqa: E501
        :type: str
        """
        self._full_font_name = full_font_name

    @property
    def version(self):
        """Gets the version of this FontInfo.  # noqa: E501

        Gets or sets the version string of the font.  # noqa: E501

        :return: The version of this FontInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FontInfo.

        Gets or sets the version string of the font.  # noqa: E501

        :param version: The version of this FontInfo.  # noqa: E501
        :type: str
        """
        self._version = version


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
        if not isinstance(other, FontInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other