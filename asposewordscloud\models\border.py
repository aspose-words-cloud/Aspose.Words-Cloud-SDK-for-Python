# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="border.py">
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

class Border(object):
    """Represents a border of an object. Borders can be applied to various document elements including paragraph, run of text inside a paragraph or a table cell.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'border_type': 'str',
        'color': 'XmlColor',
        'distance_from_text': 'float',
        'line_style': 'str',
        'line_width': 'float',
        'shadow': 'bool'
    }

    attribute_map = {
        'link': 'Link',
        'border_type': 'BorderType',
        'color': 'Color',
        'distance_from_text': 'DistanceFromText',
        'line_style': 'LineStyle',
        'line_width': 'LineWidth',
        'shadow': 'Shadow'
    }

    def __init__(self, link=None, border_type=None, color=None, distance_from_text=None, line_style=None, line_width=None, shadow=None):  # noqa: E501
        """Border - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._border_type = None
        self._color = None
        self._distance_from_text = None
        self._line_style = None
        self._line_width = None
        self._shadow = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if border_type is not None:
            self.border_type = border_type
        if color is not None:
            self.color = color
        if distance_from_text is not None:
            self.distance_from_text = distance_from_text
        if line_style is not None:
            self.line_style = line_style
        if line_width is not None:
            self.line_width = line_width
        if shadow is not None:
            self.shadow = shadow

    @property
    def link(self):
        """Gets the link of this Border.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this Border.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Border.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this Border.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def border_type(self):
        """Gets the border_type of this Border.  # noqa: E501

        Gets or sets the border type.  # noqa: E501

        :return: The border_type of this Border.  # noqa: E501
        :rtype: str
        """
        return self._border_type

    @border_type.setter
    def border_type(self, border_type):
        """Sets the border_type of this Border.

        Gets or sets the border type.  # noqa: E501

        :param border_type: The border_type of this Border.  # noqa: E501
        :type: str
        """
        allowed_values = ["Bottom", "Left", "Right", "Top", "Horizontal", "Vertical", "DiagonalDown", "DiagonalUp", "None"]  # noqa: E501
        if not border_type.isdigit():
            if border_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `border_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(border_type, allowed_values))
            self._border_type = border_type
        else:
            self._border_type = allowed_values[int(border_type) if six.PY3 else long(border_type)]

    @property
    def color(self):
        """Gets the color of this Border.  # noqa: E501

        Gets or sets the border color.  # noqa: E501

        :return: The color of this Border.  # noqa: E501
        :rtype: XmlColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Border.

        Gets or sets the border color.  # noqa: E501

        :param color: The color of this Border.  # noqa: E501
        :type: XmlColor
        """
        self._color = color

    @property
    def distance_from_text(self):
        """Gets the distance_from_text of this Border.  # noqa: E501

        Gets or sets the distance of the border from text or from the page edge in points. Has no effect and will be automatically reset to zero for borders of table cells.  # noqa: E501

        :return: The distance_from_text of this Border.  # noqa: E501
        :rtype: float
        """
        return self._distance_from_text

    @distance_from_text.setter
    def distance_from_text(self, distance_from_text):
        """Sets the distance_from_text of this Border.

        Gets or sets the distance of the border from text or from the page edge in points. Has no effect and will be automatically reset to zero for borders of table cells.  # noqa: E501

        :param distance_from_text: The distance_from_text of this Border.  # noqa: E501
        :type: float
        """
        self._distance_from_text = distance_from_text

    @property
    def line_style(self):
        """Gets the line_style of this Border.  # noqa: E501

        Gets or sets the border style. If you set line style to none, then line width is automatically changed to zero.  # noqa: E501

        :return: The line_style of this Border.  # noqa: E501
        :rtype: str
        """
        return self._line_style

    @line_style.setter
    def line_style(self, line_style):
        """Sets the line_style of this Border.

        Gets or sets the border style. If you set line style to none, then line width is automatically changed to zero.  # noqa: E501

        :param line_style: The line_style of this Border.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Single", "Thick", "Double", "Hairline", "Dot", "DashLargeGap", "DotDash", "DotDotDash", "Triple", "ThinThickSmallGap", "ThickThinSmallGap", "ThinThickThinSmallGap", "ThinThickMediumGap", "ThickThinMediumGap", "ThinThickThinMediumGap", "ThinThickLargeGap", "ThickThinLargeGap", "ThinThickThinLargeGap", "Wave", "DoubleWave", "DashSmallGap", "DashDotStroker", "Emboss3D", "Engrave3D", "Outset", "Inset"]  # noqa: E501
        if not line_style.isdigit():
            if line_style not in allowed_values:
                raise ValueError(
                    "Invalid value for `line_style` ({0}), must be one of {1}"  # noqa: E501
                    .format(line_style, allowed_values))
            self._line_style = line_style
        else:
            self._line_style = allowed_values[int(line_style) if six.PY3 else long(line_style)]

    @property
    def line_width(self):
        """Gets the line_width of this Border.  # noqa: E501

        Gets or sets the border width in points. If you set line width greater than zero when line style is none, the line style is automatically changed to single line.  # noqa: E501

        :return: The line_width of this Border.  # noqa: E501
        :rtype: float
        """
        return self._line_width

    @line_width.setter
    def line_width(self, line_width):
        """Sets the line_width of this Border.

        Gets or sets the border width in points. If you set line width greater than zero when line style is none, the line style is automatically changed to single line.  # noqa: E501

        :param line_width: The line_width of this Border.  # noqa: E501
        :type: float
        """
        self._line_width = line_width

    @property
    def shadow(self):
        """Gets the shadow of this Border.  # noqa: E501

        Gets or sets a value indicating whether the border has a shadow. In Microsoft Word, for a border to have a shadow, the borders on all four sides (left, top, right and bottom) should be of the same type, width, color and all should have the Shadow property set to true.  # noqa: E501

        :return: The shadow of this Border.  # noqa: E501
        :rtype: bool
        """
        return self._shadow

    @shadow.setter
    def shadow(self, shadow):
        """Sets the shadow of this Border.

        Gets or sets a value indicating whether the border has a shadow. In Microsoft Word, for a border to have a shadow, the borders on all four sides (left, top, right and bottom) should be of the same type, width, color and all should have the Shadow property set to true.  # noqa: E501

        :param shadow: The shadow of this Border.  # noqa: E501
        :type: bool
        """
        self._shadow = shadow


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()




        if self._color is not None:
            self._color.validate()






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
        if not isinstance(other, Border):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other