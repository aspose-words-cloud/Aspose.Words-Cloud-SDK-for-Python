# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="available_fonts_response.py">
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

class AvailableFontsResponse(object):
    """The REST response with data on system, additional and custom fonts, available for document processing.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'additional_fonts': 'list[FontInfo]',
        'custom_fonts': 'list[FontInfo]',
        'system_fonts': 'list[FontInfo]'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'additional_fonts': 'AdditionalFonts',
        'custom_fonts': 'CustomFonts',
        'system_fonts': 'SystemFonts'
    }

    def __init__(self, request_id=None, additional_fonts=None, custom_fonts=None, system_fonts=None):  # noqa: E501
        """AvailableFontsResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._additional_fonts = None
        self._custom_fonts = None
        self._system_fonts = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if additional_fonts is not None:
            self.additional_fonts = additional_fonts
        if custom_fonts is not None:
            self.custom_fonts = custom_fonts
        if system_fonts is not None:
            self.system_fonts = system_fonts

    @property
    def request_id(self):
        """Gets the request_id of this AvailableFontsResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this AvailableFontsResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AvailableFontsResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this AvailableFontsResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def additional_fonts(self):
        """Gets the additional_fonts of this AvailableFontsResponse.  # noqa: E501

        Gets or sets the list of additional fonts, provided by Aspose team.  # noqa: E501

        :return: The additional_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._additional_fonts

    @additional_fonts.setter
    def additional_fonts(self, additional_fonts):
        """Sets the additional_fonts of this AvailableFontsResponse.

        Gets or sets the list of additional fonts, provided by Aspose team.  # noqa: E501

        :param additional_fonts: The additional_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._additional_fonts = additional_fonts

    @property
    def custom_fonts(self):
        """Gets the custom_fonts of this AvailableFontsResponse.  # noqa: E501

        Gets or sets the list of custom user fonts from user cloud storage. To use them, you should specify "fontsLocation" parameter in any request.  # noqa: E501

        :return: The custom_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._custom_fonts

    @custom_fonts.setter
    def custom_fonts(self, custom_fonts):
        """Sets the custom_fonts of this AvailableFontsResponse.

        Gets or sets the list of custom user fonts from user cloud storage. To use them, you should specify "fontsLocation" parameter in any request.  # noqa: E501

        :param custom_fonts: The custom_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._custom_fonts = custom_fonts

    @property
    def system_fonts(self):
        """Gets the system_fonts of this AvailableFontsResponse.  # noqa: E501

        Gets or sets the list of system fonts, available on the server.  # noqa: E501

        :return: The system_fonts of this AvailableFontsResponse.  # noqa: E501
        :rtype: list[FontInfo]
        """
        return self._system_fonts

    @system_fonts.setter
    def system_fonts(self, system_fonts):
        """Sets the system_fonts of this AvailableFontsResponse.

        Gets or sets the list of system fonts, available on the server.  # noqa: E501

        :param system_fonts: The system_fonts of this AvailableFontsResponse.  # noqa: E501
        :type: list[FontInfo]
        """
        self._system_fonts = system_fonts


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._additional_fonts is not None:
            for elementAdditionalFonts in self._additional_fonts:
                if elementAdditionalFonts is not None:
                    elementAdditionalFonts.validate()



        if self._custom_fonts is not None:
            for elementCustomFonts in self._custom_fonts:
                if elementCustomFonts is not None:
                    elementCustomFonts.validate()



        if self._system_fonts is not None:
            for elementSystemFonts in self._system_fonts:
                if elementSystemFonts is not None:
                    elementSystemFonts.validate()


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
        if not isinstance(other, AvailableFontsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other