# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="watermark_data_text.py">
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

class WatermarkDataText(object):
    """Class for insert watermark text request building.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'color': 'XmlColor',
        'font_family': 'str',
        'font_size': 'float',
        'is_semitrasparent': 'bool',
        'layout': 'str',
        'text': 'str'
    }

    attribute_map = {
        'color': 'Color',
        'font_family': 'FontFamily',
        'font_size': 'FontSize',
        'is_semitrasparent': 'IsSemitrasparent',
        'layout': 'Layout',
        'text': 'Text'
    }

    def __init__(self, color=None, font_family=None, font_size=None, is_semitrasparent=None, layout=None, text=None):  # noqa: E501
        """WatermarkDataText - a model defined in Swagger"""  # noqa: E501

        self._color = None
        self._font_family = None
        self._font_size = None
        self._is_semitrasparent = None
        self._layout = None
        self._text = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if font_family is not None:
            self.font_family = font_family
        if font_size is not None:
            self.font_size = font_size
        if is_semitrasparent is not None:
            self.is_semitrasparent = is_semitrasparent
        if layout is not None:
            self.layout = layout
        if text is not None:
            self.text = text

    @property
    def color(self):
        """Gets the color of this WatermarkDataText.  # noqa: E501

        Gets or sets font color. The default value is System.Drawing.Color.Silver.  # noqa: E501

        :return: The color of this WatermarkDataText.  # noqa: E501
        :rtype: XmlColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this WatermarkDataText.

        Gets or sets font color. The default value is System.Drawing.Color.Silver.  # noqa: E501

        :param color: The color of this WatermarkDataText.  # noqa: E501
        :type: XmlColor
        """
        self._color = color

    @property
    def font_family(self):
        """Gets the font_family of this WatermarkDataText.  # noqa: E501

        Gets or sets font family name. The default value is "Calibri".  # noqa: E501

        :return: The font_family of this WatermarkDataText.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this WatermarkDataText.

        Gets or sets font family name. The default value is "Calibri".  # noqa: E501

        :param font_family: The font_family of this WatermarkDataText.  # noqa: E501
        :type: str
        """
        self._font_family = font_family

    @property
    def font_size(self):
        """Gets the font_size of this WatermarkDataText.  # noqa: E501

        Gets or sets a font size. The default value is 0 - auto. Valid values range from 0 to 65.5 inclusive. Auto font size means that the watermark will be scaled to its max width and max height relative to the page margins.  # noqa: E501

        :return: The font_size of this WatermarkDataText.  # noqa: E501
        :rtype: float
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this WatermarkDataText.

        Gets or sets a font size. The default value is 0 - auto. Valid values range from 0 to 65.5 inclusive. Auto font size means that the watermark will be scaled to its max width and max height relative to the page margins.  # noqa: E501

        :param font_size: The font_size of this WatermarkDataText.  # noqa: E501
        :type: float
        """
        self._font_size = font_size

    @property
    def is_semitrasparent(self):
        """Gets the is_semitrasparent of this WatermarkDataText.  # noqa: E501

        Gets or sets a boolean value which is responsible for opacity of the watermark. The default value is true.  # noqa: E501

        :return: The is_semitrasparent of this WatermarkDataText.  # noqa: E501
        :rtype: bool
        """
        return self._is_semitrasparent

    @is_semitrasparent.setter
    def is_semitrasparent(self, is_semitrasparent):
        """Sets the is_semitrasparent of this WatermarkDataText.

        Gets or sets a boolean value which is responsible for opacity of the watermark. The default value is true.  # noqa: E501

        :param is_semitrasparent: The is_semitrasparent of this WatermarkDataText.  # noqa: E501
        :type: bool
        """
        self._is_semitrasparent = is_semitrasparent

    @property
    def layout(self):
        """Gets the layout of this WatermarkDataText.  # noqa: E501

        Gets or sets layout of the watermark. The default value is Aspose.Words.WatermarkLayout.Diagonal.  # noqa: E501

        :return: The layout of this WatermarkDataText.  # noqa: E501
        :rtype: str
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this WatermarkDataText.

        Gets or sets layout of the watermark. The default value is Aspose.Words.WatermarkLayout.Diagonal.  # noqa: E501

        :param layout: The layout of this WatermarkDataText.  # noqa: E501
        :type: str
        """
        allowed_values = ["Horizontal", "Diagonal"]  # noqa: E501
        if not layout.isdigit():
            if layout not in allowed_values:
                raise ValueError(
                    "Invalid value for `layout` ({0}), must be one of {1}"  # noqa: E501
                    .format(layout, allowed_values))
            self._layout = layout
        else:
            self._layout = allowed_values[int(layout) if six.PY3 else long(layout)]

    @property
    def text(self):
        """Gets the text of this WatermarkDataText.  # noqa: E501

        Gets or sets the watermark text.  # noqa: E501

        :return: The text of this WatermarkDataText.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WatermarkDataText.

        Gets or sets the watermark text.  # noqa: E501

        :param text: The text of this WatermarkDataText.  # noqa: E501
        :type: str
        """
        self._text = text


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._text is None:
            raise ValueError("Property Text in WatermarkDataText is required.")  # noqa: E501

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
        if not isinstance(other, WatermarkDataText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other