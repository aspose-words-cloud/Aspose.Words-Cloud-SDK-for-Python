# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="shading.py">
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

class Shading(object):
    """DTO container with a paragraph format shading element.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'background_pattern_color': 'XmlColor',
        'foreground_pattern_color': 'XmlColor',
        'texture': 'str'
    }

    attribute_map = {
        'background_pattern_color': 'BackgroundPatternColor',
        'foreground_pattern_color': 'ForegroundPatternColor',
        'texture': 'Texture'
    }

    def __init__(self, background_pattern_color=None, foreground_pattern_color=None, texture=None):  # noqa: E501
        """Shading - a model defined in Swagger"""  # noqa: E501

        self._background_pattern_color = None
        self._foreground_pattern_color = None
        self._texture = None
        self.discriminator = None

        if background_pattern_color is not None:
            self.background_pattern_color = background_pattern_color
        if foreground_pattern_color is not None:
            self.foreground_pattern_color = foreground_pattern_color
        if texture is not None:
            self.texture = texture

    @property
    def background_pattern_color(self):
        """Gets the background_pattern_color of this Shading.  # noqa: E501

        Gets or sets the color that's applied to the background of the Shading object.  # noqa: E501

        :return: The background_pattern_color of this Shading.  # noqa: E501
        :rtype: XmlColor
        """
        return self._background_pattern_color

    @background_pattern_color.setter
    def background_pattern_color(self, background_pattern_color):
        """Sets the background_pattern_color of this Shading.

        Gets or sets the color that's applied to the background of the Shading object.  # noqa: E501

        :param background_pattern_color: The background_pattern_color of this Shading.  # noqa: E501
        :type: XmlColor
        """
        self._background_pattern_color = background_pattern_color

    @property
    def foreground_pattern_color(self):
        """Gets the foreground_pattern_color of this Shading.  # noqa: E501

        Gets or sets the color that's applied to the foreground of the Shading object.  # noqa: E501

        :return: The foreground_pattern_color of this Shading.  # noqa: E501
        :rtype: XmlColor
        """
        return self._foreground_pattern_color

    @foreground_pattern_color.setter
    def foreground_pattern_color(self, foreground_pattern_color):
        """Sets the foreground_pattern_color of this Shading.

        Gets or sets the color that's applied to the foreground of the Shading object.  # noqa: E501

        :param foreground_pattern_color: The foreground_pattern_color of this Shading.  # noqa: E501
        :type: XmlColor
        """
        self._foreground_pattern_color = foreground_pattern_color

    @property
    def texture(self):
        """Gets the texture of this Shading.  # noqa: E501

        Gets or sets the shading texture.  # noqa: E501

        :return: The texture of this Shading.  # noqa: E501
        :rtype: str
        """
        return self._texture

    @texture.setter
    def texture(self, texture):
        """Sets the texture of this Shading.

        Gets or sets the shading texture.  # noqa: E501

        :param texture: The texture of this Shading.  # noqa: E501
        :type: str
        """
        allowed_values = ["TextureNone", "TextureSolid", "Texture5Percent", "Texture10Percent", "Texture20Percent", "Texture25Percent", "Texture30Percent", "Texture40Percent", "Texture50Percent", "Texture60Percent", "Texture70Percent", "Texture75Percent", "Texture80Percent", "Texture90Percent", "TextureDarkHorizontal", "TextureDarkVertical", "TextureDarkDiagonalDown", "TextureDarkDiagonalUp", "TextureDarkCross", "TextureDarkDiagonalCross", "TextureHorizontal", "TextureVertical", "TextureDiagonalDown", "TextureDiagonalUp", "TextureCross", "TextureDiagonalCross", "Texture2Pt5Percent", "Texture7Pt5Percent", "Texture12Pt5Percent", "Texture15Percent", "Texture17Pt5Percent", "Texture22Pt5Percent", "Texture27Pt5Percent", "Texture32Pt5Percent", "Texture35Percent", "Texture37Pt5Percent", "Texture42Pt5Percent", "Texture45Percent", "Texture47Pt5Percent", "Texture52Pt5Percent", "Texture55Percent", "Texture57Pt5Percent", "Texture62Pt5Percent", "Texture65Percent", "Texture67Pt5Percent", "Texture72Pt5Percent", "Texture77Pt5Percent", "Texture82Pt5Percent", "Texture85Percent", "Texture87Pt5Percent", "Texture92Pt5Percent", "Texture95Percent", "Texture97Pt5Percent", "TextureNil"]  # noqa: E501
        if not texture.isdigit():
            if texture not in allowed_values:
                raise ValueError(
                    "Invalid value for `texture` ({0}), must be one of {1}"  # noqa: E501
                    .format(texture, allowed_values))
            self._texture = texture
        else:
            self._texture = allowed_values[int(texture) if six.PY3 else long(texture)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._background_pattern_color is not None:
            self._background_pattern_color.validate()



        if self._foreground_pattern_color is not None:
            self._foreground_pattern_color.validate()



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
        if not isinstance(other, Shading):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other