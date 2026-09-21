# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_cell_format.py">
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

class TableCellFormat(object):
    """DTO container with all formatting for a table row.
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
        'bottom_padding': 'float',
        'fit_text': 'bool',
        'horizontal_merge': 'str',
        'left_padding': 'float',
        'orientation': 'str',
        'preferred_width': 'PreferredWidth',
        'right_padding': 'float',
        'top_padding': 'float',
        'vertical_alignment': 'str',
        'vertical_merge': 'str',
        'width': 'float',
        'wrap_text': 'bool'
    }

    attribute_map = {
        'link': 'Link',
        'bottom_padding': 'BottomPadding',
        'fit_text': 'FitText',
        'horizontal_merge': 'HorizontalMerge',
        'left_padding': 'LeftPadding',
        'orientation': 'Orientation',
        'preferred_width': 'PreferredWidth',
        'right_padding': 'RightPadding',
        'top_padding': 'TopPadding',
        'vertical_alignment': 'VerticalAlignment',
        'vertical_merge': 'VerticalMerge',
        'width': 'Width',
        'wrap_text': 'WrapText'
    }

    def __init__(self, link=None, bottom_padding=None, fit_text=None, horizontal_merge=None, left_padding=None, orientation=None, preferred_width=None, right_padding=None, top_padding=None, vertical_alignment=None, vertical_merge=None, width=None, wrap_text=None):  # noqa: E501
        """TableCellFormat - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._bottom_padding = None
        self._fit_text = None
        self._horizontal_merge = None
        self._left_padding = None
        self._orientation = None
        self._preferred_width = None
        self._right_padding = None
        self._top_padding = None
        self._vertical_alignment = None
        self._vertical_merge = None
        self._width = None
        self._wrap_text = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if bottom_padding is not None:
            self.bottom_padding = bottom_padding
        if fit_text is not None:
            self.fit_text = fit_text
        if horizontal_merge is not None:
            self.horizontal_merge = horizontal_merge
        if left_padding is not None:
            self.left_padding = left_padding
        if orientation is not None:
            self.orientation = orientation
        if preferred_width is not None:
            self.preferred_width = preferred_width
        if right_padding is not None:
            self.right_padding = right_padding
        if top_padding is not None:
            self.top_padding = top_padding
        if vertical_alignment is not None:
            self.vertical_alignment = vertical_alignment
        if vertical_merge is not None:
            self.vertical_merge = vertical_merge
        if width is not None:
            self.width = width
        if wrap_text is not None:
            self.wrap_text = wrap_text

    @property
    def link(self):
        """Gets the link of this TableCellFormat.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this TableCellFormat.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TableCellFormat.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this TableCellFormat.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def bottom_padding(self):
        """Gets the bottom_padding of this TableCellFormat.  # noqa: E501

        Gets or sets the amount of space (in points) to add below the contents of the cell.  # noqa: E501

        :return: The bottom_padding of this TableCellFormat.  # noqa: E501
        :rtype: float
        """
        return self._bottom_padding

    @bottom_padding.setter
    def bottom_padding(self, bottom_padding):
        """Sets the bottom_padding of this TableCellFormat.

        Gets or sets the amount of space (in points) to add below the contents of the cell.  # noqa: E501

        :param bottom_padding: The bottom_padding of this TableCellFormat.  # noqa: E501
        :type: float
        """
        self._bottom_padding = bottom_padding

    @property
    def fit_text(self):
        """Gets the fit_text of this TableCellFormat.  # noqa: E501

        Gets or sets a value indicating whether to fit text in the cell, compress each paragraph to the width of the cell.  # noqa: E501

        :return: The fit_text of this TableCellFormat.  # noqa: E501
        :rtype: bool
        """
        return self._fit_text

    @fit_text.setter
    def fit_text(self, fit_text):
        """Sets the fit_text of this TableCellFormat.

        Gets or sets a value indicating whether to fit text in the cell, compress each paragraph to the width of the cell.  # noqa: E501

        :param fit_text: The fit_text of this TableCellFormat.  # noqa: E501
        :type: bool
        """
        self._fit_text = fit_text

    @property
    def horizontal_merge(self):
        """Gets the horizontal_merge of this TableCellFormat.  # noqa: E501

        Gets or sets the option that controls how the cell is merged horizontally with other cells in the row.  # noqa: E501

        :return: The horizontal_merge of this TableCellFormat.  # noqa: E501
        :rtype: str
        """
        return self._horizontal_merge

    @horizontal_merge.setter
    def horizontal_merge(self, horizontal_merge):
        """Sets the horizontal_merge of this TableCellFormat.

        Gets or sets the option that controls how the cell is merged horizontally with other cells in the row.  # noqa: E501

        :param horizontal_merge: The horizontal_merge of this TableCellFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "First", "Previous"]  # noqa: E501
        if not horizontal_merge.isdigit():
            if horizontal_merge not in allowed_values:
                raise ValueError(
                    "Invalid value for `horizontal_merge` ({0}), must be one of {1}"  # noqa: E501
                    .format(horizontal_merge, allowed_values))
            self._horizontal_merge = horizontal_merge
        else:
            self._horizontal_merge = allowed_values[int(horizontal_merge) if six.PY3 else long(horizontal_merge)]

    @property
    def left_padding(self):
        """Gets the left_padding of this TableCellFormat.  # noqa: E501

        Gets or sets the amount of space (in points) to add to the left of the contents of the cell.  # noqa: E501

        :return: The left_padding of this TableCellFormat.  # noqa: E501
        :rtype: float
        """
        return self._left_padding

    @left_padding.setter
    def left_padding(self, left_padding):
        """Sets the left_padding of this TableCellFormat.

        Gets or sets the amount of space (in points) to add to the left of the contents of the cell.  # noqa: E501

        :param left_padding: The left_padding of this TableCellFormat.  # noqa: E501
        :type: float
        """
        self._left_padding = left_padding

    @property
    def orientation(self):
        """Gets the orientation of this TableCellFormat.  # noqa: E501

        Gets or sets the orientation of text in a table cell.  # noqa: E501

        :return: The orientation of this TableCellFormat.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this TableCellFormat.

        Gets or sets the orientation of text in a table cell.  # noqa: E501

        :param orientation: The orientation of this TableCellFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["Horizontal", "Downward", "Upward", "HorizontalRotatedFarEast", "VerticalFarEast", "VerticalRotatedFarEast"]  # noqa: E501
        if not orientation.isdigit():
            if orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation, allowed_values))
            self._orientation = orientation
        else:
            self._orientation = allowed_values[int(orientation) if six.PY3 else long(orientation)]

    @property
    def preferred_width(self):
        """Gets the preferred_width of this TableCellFormat.  # noqa: E501

        Gets or sets the preferred width of the cell. The preferred width (along with the table's Auto Fit option) determines how the actual width of the cell is calculated by the table layout algorithm. Table layout can be performed by Aspose.Words when it saves the document or by Microsoft Word when it displays the document.The preferred width can be specified in points or in percent. The preferred width can also be specified as "auto", which means no preferred width is specified.The default value is Auto.  # noqa: E501

        :return: The preferred_width of this TableCellFormat.  # noqa: E501
        :rtype: PreferredWidth
        """
        return self._preferred_width

    @preferred_width.setter
    def preferred_width(self, preferred_width):
        """Sets the preferred_width of this TableCellFormat.

        Gets or sets the preferred width of the cell. The preferred width (along with the table's Auto Fit option) determines how the actual width of the cell is calculated by the table layout algorithm. Table layout can be performed by Aspose.Words when it saves the document or by Microsoft Word when it displays the document.The preferred width can be specified in points or in percent. The preferred width can also be specified as "auto", which means no preferred width is specified.The default value is Auto.  # noqa: E501

        :param preferred_width: The preferred_width of this TableCellFormat.  # noqa: E501
        :type: PreferredWidth
        """
        self._preferred_width = preferred_width

    @property
    def right_padding(self):
        """Gets the right_padding of this TableCellFormat.  # noqa: E501

        Gets or sets the amount of space (in points) to add to the right of the contents of the cell.  # noqa: E501

        :return: The right_padding of this TableCellFormat.  # noqa: E501
        :rtype: float
        """
        return self._right_padding

    @right_padding.setter
    def right_padding(self, right_padding):
        """Sets the right_padding of this TableCellFormat.

        Gets or sets the amount of space (in points) to add to the right of the contents of the cell.  # noqa: E501

        :param right_padding: The right_padding of this TableCellFormat.  # noqa: E501
        :type: float
        """
        self._right_padding = right_padding

    @property
    def top_padding(self):
        """Gets the top_padding of this TableCellFormat.  # noqa: E501

        Gets or sets the amount of space (in points) to add above the contents of the cell.  # noqa: E501

        :return: The top_padding of this TableCellFormat.  # noqa: E501
        :rtype: float
        """
        return self._top_padding

    @top_padding.setter
    def top_padding(self, top_padding):
        """Sets the top_padding of this TableCellFormat.

        Gets or sets the amount of space (in points) to add above the contents of the cell.  # noqa: E501

        :param top_padding: The top_padding of this TableCellFormat.  # noqa: E501
        :type: float
        """
        self._top_padding = top_padding

    @property
    def vertical_alignment(self):
        """Gets the vertical_alignment of this TableCellFormat.  # noqa: E501

        Gets or sets the vertical alignment of text in the cell.  # noqa: E501

        :return: The vertical_alignment of this TableCellFormat.  # noqa: E501
        :rtype: str
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """Sets the vertical_alignment of this TableCellFormat.

        Gets or sets the vertical alignment of text in the cell.  # noqa: E501

        :param vertical_alignment: The vertical_alignment of this TableCellFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["Top", "Center", "Bottom"]  # noqa: E501
        if not vertical_alignment.isdigit():
            if vertical_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `vertical_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(vertical_alignment, allowed_values))
            self._vertical_alignment = vertical_alignment
        else:
            self._vertical_alignment = allowed_values[int(vertical_alignment) if six.PY3 else long(vertical_alignment)]

    @property
    def vertical_merge(self):
        """Gets the vertical_merge of this TableCellFormat.  # noqa: E501

        Gets or sets the option that controls how the cell is merged with other cells vertically. Cells can only be merged vertically if their left and right boundaries are identical.When cells are vertically merged, the display areas of the merged cells are consolidated. The consolidated area is used to display the contents of the first vertically merged cell and all other vertically merged cells must be empty.  # noqa: E501

        :return: The vertical_merge of this TableCellFormat.  # noqa: E501
        :rtype: str
        """
        return self._vertical_merge

    @vertical_merge.setter
    def vertical_merge(self, vertical_merge):
        """Sets the vertical_merge of this TableCellFormat.

        Gets or sets the option that controls how the cell is merged with other cells vertically. Cells can only be merged vertically if their left and right boundaries are identical.When cells are vertically merged, the display areas of the merged cells are consolidated. The consolidated area is used to display the contents of the first vertically merged cell and all other vertically merged cells must be empty.  # noqa: E501

        :param vertical_merge: The vertical_merge of this TableCellFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "First", "Previous"]  # noqa: E501
        if not vertical_merge.isdigit():
            if vertical_merge not in allowed_values:
                raise ValueError(
                    "Invalid value for `vertical_merge` ({0}), must be one of {1}"  # noqa: E501
                    .format(vertical_merge, allowed_values))
            self._vertical_merge = vertical_merge
        else:
            self._vertical_merge = allowed_values[int(vertical_merge) if six.PY3 else long(vertical_merge)]

    @property
    def width(self):
        """Gets the width of this TableCellFormat.  # noqa: E501

        Gets or sets the width of the cell in points. The width is calculated by Aspose.Words on document loading and saving. Currently, not every combination of table, cell and document properties is supported. The returned value may not be accurate for some documents. It may not exactly match the cell width as calculated by MS Word when the document is opened in MS Word.Setting this property is not recommended. There is no guarantee that the cell will actually have the set width. The width may be adjusted to accommodate cell contents in an auto-fit table layout. Cells in other rows may have conflicting width settings. The table may be resized to fit into the container or to meet table width settings. Consider using PreferredWidth for setting the cell width. Setting this property sets PreferredWidth implicitly since version 15.8.  # noqa: E501

        :return: The width of this TableCellFormat.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TableCellFormat.

        Gets or sets the width of the cell in points. The width is calculated by Aspose.Words on document loading and saving. Currently, not every combination of table, cell and document properties is supported. The returned value may not be accurate for some documents. It may not exactly match the cell width as calculated by MS Word when the document is opened in MS Word.Setting this property is not recommended. There is no guarantee that the cell will actually have the set width. The width may be adjusted to accommodate cell contents in an auto-fit table layout. Cells in other rows may have conflicting width settings. The table may be resized to fit into the container or to meet table width settings. Consider using PreferredWidth for setting the cell width. Setting this property sets PreferredWidth implicitly since version 15.8.  # noqa: E501

        :param width: The width of this TableCellFormat.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def wrap_text(self):
        """Gets the wrap_text of this TableCellFormat.  # noqa: E501

        Gets or sets a value indicating whether to wrap text in the cell.  # noqa: E501

        :return: The wrap_text of this TableCellFormat.  # noqa: E501
        :rtype: bool
        """
        return self._wrap_text

    @wrap_text.setter
    def wrap_text(self, wrap_text):
        """Sets the wrap_text of this TableCellFormat.

        Gets or sets a value indicating whether to wrap text in the cell.  # noqa: E501

        :param wrap_text: The wrap_text of this TableCellFormat.  # noqa: E501
        :type: bool
        """
        self._wrap_text = wrap_text


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()








        if self._preferred_width is not None:
            self._preferred_width.validate()








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
        if not isinstance(other, TableCellFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other