# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="drawing_object.py">
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

class DrawingObject(object):
    """DTO container with a DrawingObject.
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
        'node_id': 'str',
        'render_links': 'list[WordsApiLink]',
        'width': 'float',
        'height': 'float',
        'ole_data_link': 'WordsApiLink',
        'image_data_link': 'WordsApiLink',
        'relative_horizontal_position': 'str',
        'left': 'float',
        'relative_vertical_position': 'str',
        'top': 'float',
        'wrap_type': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'render_links': 'RenderLinks',
        'width': 'Width',
        'height': 'Height',
        'ole_data_link': 'OleDataLink',
        'image_data_link': 'ImageDataLink',
        'relative_horizontal_position': 'RelativeHorizontalPosition',
        'left': 'Left',
        'relative_vertical_position': 'RelativeVerticalPosition',
        'top': 'Top',
        'wrap_type': 'WrapType'
    }

    def __init__(self, link=None, node_id=None, render_links=None, width=None, height=None, ole_data_link=None, image_data_link=None, relative_horizontal_position=None, left=None, relative_vertical_position=None, top=None, wrap_type=None):  # noqa: E501
        """DrawingObject - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._render_links = None
        self._width = None
        self._height = None
        self._ole_data_link = None
        self._image_data_link = None
        self._relative_horizontal_position = None
        self._left = None
        self._relative_vertical_position = None
        self._top = None
        self._wrap_type = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if render_links is not None:
            self.render_links = render_links
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if ole_data_link is not None:
            self.ole_data_link = ole_data_link
        if image_data_link is not None:
            self.image_data_link = image_data_link
        if relative_horizontal_position is not None:
            self.relative_horizontal_position = relative_horizontal_position
        if left is not None:
            self.left = left
        if relative_vertical_position is not None:
            self.relative_vertical_position = relative_vertical_position
        if top is not None:
            self.top = top
        if wrap_type is not None:
            self.wrap_type = wrap_type

    @property
    def link(self):
        """Gets the link of this DrawingObject.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this DrawingObject.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this DrawingObject.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this DrawingObject.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this DrawingObject.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this DrawingObject.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DrawingObject.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this DrawingObject.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def render_links(self):
        """Gets the render_links of this DrawingObject.  # noqa: E501

        Gets or sets the list of links that originate from this DrawingObjectDto.  # noqa: E501

        :return: The render_links of this DrawingObject.  # noqa: E501
        :rtype: list[WordsApiLink]
        """
        return self._render_links

    @render_links.setter
    def render_links(self, render_links):
        """Sets the render_links of this DrawingObject.

        Gets or sets the list of links that originate from this DrawingObjectDto.  # noqa: E501

        :param render_links: The render_links of this DrawingObject.  # noqa: E501
        :type: list[WordsApiLink]
        """
        self._render_links = render_links

    @property
    def width(self):
        """Gets the width of this DrawingObject.  # noqa: E501

        Gets or sets the width of the DrawingObjects in points.  # noqa: E501

        :return: The width of this DrawingObject.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DrawingObject.

        Gets or sets the width of the DrawingObjects in points.  # noqa: E501

        :param width: The width of this DrawingObject.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this DrawingObject.  # noqa: E501

        Gets or sets the height of the DrawingObject in points.  # noqa: E501

        :return: The height of this DrawingObject.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DrawingObject.

        Gets or sets the height of the DrawingObject in points.  # noqa: E501

        :param height: The height of this DrawingObject.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def ole_data_link(self):
        """Gets the ole_data_link of this DrawingObject.  # noqa: E501

        Gets or sets the link to OLE object. Can be null if shape does not have OLE data.  # noqa: E501

        :return: The ole_data_link of this DrawingObject.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._ole_data_link

    @ole_data_link.setter
    def ole_data_link(self, ole_data_link):
        """Sets the ole_data_link of this DrawingObject.

        Gets or sets the link to OLE object. Can be null if shape does not have OLE data.  # noqa: E501

        :param ole_data_link: The ole_data_link of this DrawingObject.  # noqa: E501
        :type: WordsApiLink
        """
        self._ole_data_link = ole_data_link

    @property
    def image_data_link(self):
        """Gets the image_data_link of this DrawingObject.  # noqa: E501

        Gets or sets the link to image data. Can be null if shape does not have an image.  # noqa: E501

        :return: The image_data_link of this DrawingObject.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._image_data_link

    @image_data_link.setter
    def image_data_link(self, image_data_link):
        """Sets the image_data_link of this DrawingObject.

        Gets or sets the link to image data. Can be null if shape does not have an image.  # noqa: E501

        :param image_data_link: The image_data_link of this DrawingObject.  # noqa: E501
        :type: WordsApiLink
        """
        self._image_data_link = image_data_link

    @property
    def relative_horizontal_position(self):
        """Gets the relative_horizontal_position of this DrawingObject.  # noqa: E501

        Gets or sets the relative horizontal position, from which the distance to the image is measured.  # noqa: E501

        :return: The relative_horizontal_position of this DrawingObject.  # noqa: E501
        :rtype: str
        """
        return self._relative_horizontal_position

    @relative_horizontal_position.setter
    def relative_horizontal_position(self, relative_horizontal_position):
        """Sets the relative_horizontal_position of this DrawingObject.

        Gets or sets the relative horizontal position, from which the distance to the image is measured.  # noqa: E501

        :param relative_horizontal_position: The relative_horizontal_position of this DrawingObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["Margin", "Page", "Column", "Default", "Character", "LeftMargin", "RightMargin", "InsideMargin", "OutsideMargin"]  # noqa: E501
        if not relative_horizontal_position.isdigit():
            if relative_horizontal_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `relative_horizontal_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(relative_horizontal_position, allowed_values))
            self._relative_horizontal_position = relative_horizontal_position
        else:
            self._relative_horizontal_position = allowed_values[int(relative_horizontal_position) if six.PY3 else long(relative_horizontal_position)]

    @property
    def left(self):
        """Gets the left of this DrawingObject.  # noqa: E501

        Gets or sets the distance in points from the origin to the left side of the image.  # noqa: E501

        :return: The left of this DrawingObject.  # noqa: E501
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this DrawingObject.

        Gets or sets the distance in points from the origin to the left side of the image.  # noqa: E501

        :param left: The left of this DrawingObject.  # noqa: E501
        :type: float
        """
        self._left = left

    @property
    def relative_vertical_position(self):
        """Gets the relative_vertical_position of this DrawingObject.  # noqa: E501

        Gets or sets the relative vertical position, from which the distance to the image is measured.  # noqa: E501

        :return: The relative_vertical_position of this DrawingObject.  # noqa: E501
        :rtype: str
        """
        return self._relative_vertical_position

    @relative_vertical_position.setter
    def relative_vertical_position(self, relative_vertical_position):
        """Sets the relative_vertical_position of this DrawingObject.

        Gets or sets the relative vertical position, from which the distance to the image is measured.  # noqa: E501

        :param relative_vertical_position: The relative_vertical_position of this DrawingObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["Margin", "TableDefault", "Page", "Paragraph", "TextFrameDefault", "Line", "TopMargin", "BottomMargin", "InsideMargin", "OutsideMargin"]  # noqa: E501
        if not relative_vertical_position.isdigit():
            if relative_vertical_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `relative_vertical_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(relative_vertical_position, allowed_values))
            self._relative_vertical_position = relative_vertical_position
        else:
            self._relative_vertical_position = allowed_values[int(relative_vertical_position) if six.PY3 else long(relative_vertical_position)]

    @property
    def top(self):
        """Gets the top of this DrawingObject.  # noqa: E501

        Gets or sets the distance in points from the origin to the top side of the image.  # noqa: E501

        :return: The top of this DrawingObject.  # noqa: E501
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this DrawingObject.

        Gets or sets the distance in points from the origin to the top side of the image.  # noqa: E501

        :param top: The top of this DrawingObject.  # noqa: E501
        :type: float
        """
        self._top = top

    @property
    def wrap_type(self):
        """Gets the wrap_type of this DrawingObject.  # noqa: E501

        Gets or sets the option that controls how to wrap text around the image.  # noqa: E501

        :return: The wrap_type of this DrawingObject.  # noqa: E501
        :rtype: str
        """
        return self._wrap_type

    @wrap_type.setter
    def wrap_type(self, wrap_type):
        """Sets the wrap_type of this DrawingObject.

        Gets or sets the option that controls how to wrap text around the image.  # noqa: E501

        :param wrap_type: The wrap_type of this DrawingObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inline", "TopBottom", "Square", "None", "Tight", "Through"]  # noqa: E501
        if not wrap_type.isdigit():
            if wrap_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `wrap_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(wrap_type, allowed_values))
            self._wrap_type = wrap_type
        else:
            self._wrap_type = allowed_values[int(wrap_type) if six.PY3 else long(wrap_type)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()




        if self._render_links is not None:
            for elementRenderLinks in self._render_links:
                if elementRenderLinks is not None:
                    elementRenderLinks.validate()





        if self._ole_data_link is not None:
            self._ole_data_link.validate()



        if self._image_data_link is not None:
            self._image_data_link.validate()







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
        if not isinstance(other, DrawingObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other