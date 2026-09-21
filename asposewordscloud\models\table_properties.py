# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table_properties.py">
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

class TableProperties(object):
    """DTO container with table properties.
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
        'alignment': 'str',
        'allow_auto_fit': 'bool',
        'bidi': 'bool',
        'bottom_padding': 'float',
        'cell_spacing': 'float',
        'left_indent': 'float',
        'left_padding': 'float',
        'preferred_width': 'PreferredWidth',
        'right_padding': 'float',
        'style_identifier': 'str',
        'style_name': 'str',
        'style_options': 'str',
        'text_wrapping': 'str',
        'top_padding': 'float'
    }

    attribute_map = {
        'link': 'Link',
        'alignment': 'Alignment',
        'allow_auto_fit': 'AllowAutoFit',
        'bidi': 'Bidi',
        'bottom_padding': 'BottomPadding',
        'cell_spacing': 'CellSpacing',
        'left_indent': 'LeftIndent',
        'left_padding': 'LeftPadding',
        'preferred_width': 'PreferredWidth',
        'right_padding': 'RightPadding',
        'style_identifier': 'StyleIdentifier',
        'style_name': 'StyleName',
        'style_options': 'StyleOptions',
        'text_wrapping': 'TextWrapping',
        'top_padding': 'TopPadding'
    }

    def __init__(self, link=None, alignment=None, allow_auto_fit=None, bidi=None, bottom_padding=None, cell_spacing=None, left_indent=None, left_padding=None, preferred_width=None, right_padding=None, style_identifier=None, style_name=None, style_options=None, text_wrapping=None, top_padding=None):  # noqa: E501
        """TableProperties - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._alignment = None
        self._allow_auto_fit = None
        self._bidi = None
        self._bottom_padding = None
        self._cell_spacing = None
        self._left_indent = None
        self._left_padding = None
        self._preferred_width = None
        self._right_padding = None
        self._style_identifier = None
        self._style_name = None
        self._style_options = None
        self._text_wrapping = None
        self._top_padding = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if alignment is not None:
            self.alignment = alignment
        if allow_auto_fit is not None:
            self.allow_auto_fit = allow_auto_fit
        if bidi is not None:
            self.bidi = bidi
        if bottom_padding is not None:
            self.bottom_padding = bottom_padding
        if cell_spacing is not None:
            self.cell_spacing = cell_spacing
        if left_indent is not None:
            self.left_indent = left_indent
        if left_padding is not None:
            self.left_padding = left_padding
        if preferred_width is not None:
            self.preferred_width = preferred_width
        if right_padding is not None:
            self.right_padding = right_padding
        if style_identifier is not None:
            self.style_identifier = style_identifier
        if style_name is not None:
            self.style_name = style_name
        if style_options is not None:
            self.style_options = style_options
        if text_wrapping is not None:
            self.text_wrapping = text_wrapping
        if top_padding is not None:
            self.top_padding = top_padding

    @property
    def link(self):
        """Gets the link of this TableProperties.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this TableProperties.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TableProperties.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this TableProperties.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def alignment(self):
        """Gets the alignment of this TableProperties.  # noqa: E501

        Gets or sets the option that controls how an inline table is aligned in the document. The default value is Left.  # noqa: E501

        :return: The alignment of this TableProperties.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this TableProperties.

        Gets or sets the option that controls how an inline table is aligned in the document. The default value is Left.  # noqa: E501

        :param alignment: The alignment of this TableProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["Left", "Center", "Right"]  # noqa: E501
        if not alignment.isdigit():
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values))
            self._alignment = alignment
        else:
            self._alignment = allowed_values[int(alignment) if six.PY3 else long(alignment)]

    @property
    def allow_auto_fit(self):
        """Gets the allow_auto_fit of this TableProperties.  # noqa: E501

        Gets or sets a value indicating whether to automatically resize cells in a table to fit their contents. The default value is true.  # noqa: E501

        :return: The allow_auto_fit of this TableProperties.  # noqa: E501
        :rtype: bool
        """
        return self._allow_auto_fit

    @allow_auto_fit.setter
    def allow_auto_fit(self, allow_auto_fit):
        """Sets the allow_auto_fit of this TableProperties.

        Gets or sets a value indicating whether to automatically resize cells in a table to fit their contents. The default value is true.  # noqa: E501

        :param allow_auto_fit: The allow_auto_fit of this TableProperties.  # noqa: E501
        :type: bool
        """
        self._allow_auto_fit = allow_auto_fit

    @property
    def bidi(self):
        """Gets the bidi of this TableProperties.  # noqa: E501

        Gets or sets a value indicating whether this is a right-to-left table. When true, the cells in this row are laid out right to left.The default value is false.  # noqa: E501

        :return: The bidi of this TableProperties.  # noqa: E501
        :rtype: bool
        """
        return self._bidi

    @bidi.setter
    def bidi(self, bidi):
        """Sets the bidi of this TableProperties.

        Gets or sets a value indicating whether this is a right-to-left table. When true, the cells in this row are laid out right to left.The default value is false.  # noqa: E501

        :param bidi: The bidi of this TableProperties.  # noqa: E501
        :type: bool
        """
        self._bidi = bidi

    @property
    def bottom_padding(self):
        """Gets the bottom_padding of this TableProperties.  # noqa: E501

        Gets or sets the amount of space (in points) to add below the contents of cells.  # noqa: E501

        :return: The bottom_padding of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._bottom_padding

    @bottom_padding.setter
    def bottom_padding(self, bottom_padding):
        """Sets the bottom_padding of this TableProperties.

        Gets or sets the amount of space (in points) to add below the contents of cells.  # noqa: E501

        :param bottom_padding: The bottom_padding of this TableProperties.  # noqa: E501
        :type: float
        """
        self._bottom_padding = bottom_padding

    @property
    def cell_spacing(self):
        """Gets the cell_spacing of this TableProperties.  # noqa: E501

        Gets or sets the amount of space (in points) between the cells.  # noqa: E501

        :return: The cell_spacing of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._cell_spacing

    @cell_spacing.setter
    def cell_spacing(self, cell_spacing):
        """Sets the cell_spacing of this TableProperties.

        Gets or sets the amount of space (in points) between the cells.  # noqa: E501

        :param cell_spacing: The cell_spacing of this TableProperties.  # noqa: E501
        :type: float
        """
        self._cell_spacing = cell_spacing

    @property
    def left_indent(self):
        """Gets the left_indent of this TableProperties.  # noqa: E501

        Gets or sets the value, that represents the left indent of the table.  # noqa: E501

        :return: The left_indent of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._left_indent

    @left_indent.setter
    def left_indent(self, left_indent):
        """Sets the left_indent of this TableProperties.

        Gets or sets the value, that represents the left indent of the table.  # noqa: E501

        :param left_indent: The left_indent of this TableProperties.  # noqa: E501
        :type: float
        """
        self._left_indent = left_indent

    @property
    def left_padding(self):
        """Gets the left_padding of this TableProperties.  # noqa: E501

        Gets or sets the amount of space (in points) to add to the left of the contents of cells.  # noqa: E501

        :return: The left_padding of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._left_padding

    @left_padding.setter
    def left_padding(self, left_padding):
        """Sets the left_padding of this TableProperties.

        Gets or sets the amount of space (in points) to add to the left of the contents of cells.  # noqa: E501

        :param left_padding: The left_padding of this TableProperties.  # noqa: E501
        :type: float
        """
        self._left_padding = left_padding

    @property
    def preferred_width(self):
        """Gets the preferred_width of this TableProperties.  # noqa: E501

        Gets or sets the table preferred width. Preferred width can be specified as a percentage, number of points or a special "auto" value.  # noqa: E501

        :return: The preferred_width of this TableProperties.  # noqa: E501
        :rtype: PreferredWidth
        """
        return self._preferred_width

    @preferred_width.setter
    def preferred_width(self, preferred_width):
        """Sets the preferred_width of this TableProperties.

        Gets or sets the table preferred width. Preferred width can be specified as a percentage, number of points or a special "auto" value.  # noqa: E501

        :param preferred_width: The preferred_width of this TableProperties.  # noqa: E501
        :type: PreferredWidth
        """
        self._preferred_width = preferred_width

    @property
    def right_padding(self):
        """Gets the right_padding of this TableProperties.  # noqa: E501

        Gets or sets the amount of space (in points) to add to the right of the contents of cells.  # noqa: E501

        :return: The right_padding of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._right_padding

    @right_padding.setter
    def right_padding(self, right_padding):
        """Sets the right_padding of this TableProperties.

        Gets or sets the amount of space (in points) to add to the right of the contents of cells.  # noqa: E501

        :param right_padding: The right_padding of this TableProperties.  # noqa: E501
        :type: float
        """
        self._right_padding = right_padding

    @property
    def style_identifier(self):
        """Gets the style_identifier of this TableProperties.  # noqa: E501

        Gets or sets the locale independent style identifier of the table style applied to this table.  # noqa: E501

        :return: The style_identifier of this TableProperties.  # noqa: E501
        :rtype: str
        """
        return self._style_identifier

    @style_identifier.setter
    def style_identifier(self, style_identifier):
        """Sets the style_identifier of this TableProperties.

        Gets or sets the locale independent style identifier of the table style applied to this table.  # noqa: E501

        :param style_identifier: The style_identifier of this TableProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["Normal", "Heading1", "Heading2", "Heading3", "Heading4", "Heading5", "Heading6", "Heading7", "Heading8", "Heading9", "Index1", "Index2", "Index3", "Index4", "Index5", "Index6", "Index7", "Index8", "Index9", "Toc1", "Toc2", "Toc3", "Toc4", "Toc5", "Toc6", "Toc7", "Toc8", "Toc9", "NormalIndent", "FootnoteText", "CommentText", "Header", "Footer", "IndexHeading", "Caption", "TableOfFigures", "EnvelopeAddress", "EnvelopeReturn", "FootnoteReference", "CommentReference", "LineNumber", "PageNumber", "EndnoteReference", "EndnoteText", "TableOfAuthorities", "Macro", "ToaHeading", "List", "ListBullet", "ListNumber", "List2", "List3", "List4", "List5", "ListBullet2", "ListBullet3", "ListBullet4", "ListBullet5", "ListNumber2", "ListNumber3", "ListNumber4", "ListNumber5", "Title", "Closing", "Signature", "DefaultParagraphFont", "BodyText", "BodyTextInd", "ListContinue", "ListContinue2", "ListContinue3", "ListContinue4", "ListContinue5", "MessageHeader", "Subtitle", "Salutation", "Date", "BodyText1I", "BodyText1I2", "NoteHeading", "BodyText2", "BodyText3", "BodyTextInd2", "BodyTextInd3", "BlockText", "Hyperlink", "FollowedHyperlink", "Strong", "Emphasis", "DocumentMap", "PlainText", "EmailSignature", "HtmlTopOfForm", "HtmlBottomOfForm", "NormalWeb", "HtmlAcronym", "HtmlAddress", "HtmlCite", "HtmlCode", "HtmlDefinition", "HtmlKeyboard", "HtmlPreformatted", "HtmlSample", "HtmlTypewriter", "HtmlVariable", "TableNormal", "CommentSubject", "NoList", "OutlineList1", "OutlineList2", "OutlineList3", "TableSimple1", "TableSimple2", "TableSimple3", "TableClassic1", "TableClassic2", "TableClassic3", "TableClassic4", "TableColorful1", "TableColorful2", "TableColorful3", "TableColumns1", "TableColumns2", "TableColumns3", "TableColumns4", "TableColumns5", "TableGrid1", "TableGrid2", "TableGrid3", "TableGrid4", "TableGrid5", "TableGrid6", "TableGrid7", "TableGrid8", "TableList1", "TableList2", "TableList3", "TableList4", "TableList5", "TableList6", "TableList7", "TableList8", "Table3DEffects1", "Table3DEffects2", "Table3DEffects3", "TableContemporary", "TableElegant", "TableProfessional", "TableSubtle1", "TableSubtle2", "TableWeb1", "TableWeb2", "TableWeb3", "BalloonText", "TableGrid", "TableTheme", "PlaceholderText", "NoSpacing", "LightShading", "LightList", "LightGrid", "MediumShading1", "MediumShading2", "MediumList1", "MediumList2", "MediumGrid1", "MediumGrid2", "MediumGrid3", "DarkList", "ColorfulShading", "ColorfulList", "ColorfulGrid", "LightShadingAccent1", "LightListAccent1", "LightGridAccent1", "MediumShading1Accent1", "MediumShading2Accent1", "MediumList1Accent1", "Revision", "ListParagraph", "Quote", "IntenseQuote", "MediumList2Accent1", "MediumGrid1Accent1", "MediumGrid2Accent1", "MediumGrid3Accent1", "DarkListAccent1", "ColorfulShadingAccent1", "ColorfulListAccent1", "ColorfulGridAccent1", "LightShadingAccent2", "LightListAccent2", "LightGridAccent2", "MediumShading1Accent2", "MediumShading2Accent2", "MediumList1Accent2", "MediumList2Accent2", "MediumGrid1Accent2", "MediumGrid2Accent2", "MediumGrid3Accent2", "DarkListAccent2", "ColorfulShadingAccent2", "ColorfulListAccent2", "ColorfulGridAccent2", "LightShadingAccent3", "LightListAccent3", "LightGridAccent3", "MediumShading1Accent3", "MediumShading2Accent3", "MediumList1Accent3", "MediumList2Accent3", "MediumGrid1Accent3", "MediumGrid2Accent3", "MediumGrid3Accent3", "DarkListAccent3", "ColorfulShadingAccent3", "ColorfulListAccent3", "ColorfulGridAccent3", "LightShadingAccent4", "LightListAccent4", "LightGridAccent4", "MediumShading1Accent4", "MediumShading2Accent4", "MediumList1Accent4", "MediumList2Accent4", "MediumGrid1Accent4", "MediumGrid2Accent4", "MediumGrid3Accent4", "DarkListAccent4", "ColorfulShadingAccent4", "ColorfulListAccent4", "ColorfulGridAccent4", "LightShadingAccent5", "LightListAccent5", "LightGridAccent5", "MediumShading1Accent5", "MediumShading2Accent5", "MediumList1Accent5", "MediumList2Accent5", "MediumGrid1Accent5", "MediumGrid2Accent5", "MediumGrid3Accent5", "DarkListAccent5", "ColorfulShadingAccent5", "ColorfulListAccent5", "ColorfulGridAccent5", "LightShadingAccent6", "LightListAccent6", "LightGridAccent6", "MediumShading1Accent6", "MediumShading2Accent6", "MediumList1Accent6", "MediumList2Accent6", "MediumGrid1Accent6", "MediumGrid2Accent6", "MediumGrid3Accent6", "DarkListAccent6", "ColorfulShadingAccent6", "ColorfulListAccent6", "ColorfulGridAccent6", "SubtleEmphasis", "IntenseEmphasis", "SubtleReference", "IntenseReference", "BookTitle", "Bibliography", "TocHeading", "PlainTable1", "PlainTable2", "PlainTable3", "PlainTable4", "PlainTable5", "TableGridLight", "GridTable1Light", "GridTable2", "GridTable3", "GridTable4", "GridTable5Dark", "GridTable6Colorful", "GridTable7Colorful", "GridTable1LightAccent1", "GridTable2Accent1", "GridTable3Accent1", "GridTable4Accent1", "GridTable5DarkAccent1", "GridTable6ColorfulAccent1", "GridTable7ColorfulAccent1", "GridTable1LightAccent2", "GridTable2Accent2", "GridTable3Accent2", "GridTable4Accent2", "GridTable5DarkAccent2", "GridTable6ColorfulAccent2", "GridTable7ColorfulAccent2", "GridTable1LightAccent3", "GridTable2Accent3", "GridTable3Accent3", "GridTable4Accent3", "GridTable5DarkAccent3", "GridTable6ColorfulAccent3", "GridTable7ColorfulAccent3", "GridTable1LightAccent4", "GridTable2Accent4", "GridTable3Accent4", "GridTable4Accent4", "GridTable5DarkAccent4", "GridTable6ColorfulAccent4", "GridTable7ColorfulAccent4", "GridTable1LightAccent5", "GridTable2Accent5", "GridTable3Accent5", "GridTable4Accent5", "GridTable5DarkAccent5", "GridTable6ColorfulAccent5", "GridTable7ColorfulAccent5", "GridTable1LightAccent6", "GridTable2Accent6", "GridTable3Accent6", "GridTable4Accent6", "GridTable5DarkAccent6", "GridTable6ColorfulAccent6", "GridTable7ColorfulAccent6", "ListTable1Light", "ListTable2", "ListTable3", "ListTable4", "ListTable5Dark", "ListTable6Colorful", "ListTable7Colorful", "ListTable1LightAccent1", "ListTable2Accent1", "ListTable3Accent1", "ListTable4Accent1", "ListTable5DarkAccent1", "ListTable6ColorfulAccent1", "ListTable7ColorfulAccent1", "ListTable1LightAccent2", "ListTable2Accent2", "ListTable3Accent2", "ListTable4Accent2", "ListTable5DarkAccent2", "ListTable6ColorfulAccent2", "ListTable7ColorfulAccent2", "ListTable1LightAccent3", "ListTable2Accent3", "ListTable3Accent3", "ListTable4Accent3", "ListTable5DarkAccent3", "ListTable6ColorfulAccent3", "ListTable7ColorfulAccent3", "ListTable1LightAccent4", "ListTable2Accent4", "ListTable3Accent4", "ListTable4Accent4", "ListTable5DarkAccent4", "ListTable6ColorfulAccent4", "ListTable7ColorfulAccent4", "ListTable1LightAccent5", "ListTable2Accent5", "ListTable3Accent5", "ListTable4Accent5", "ListTable5DarkAccent5", "ListTable6ColorfulAccent5", "ListTable7ColorfulAccent5", "ListTable1LightAccent6", "ListTable2Accent6", "ListTable3Accent6", "ListTable4Accent6", "ListTable5DarkAccent6", "ListTable6ColorfulAccent6", "ListTable7ColorfulAccent6", "SmartLink", "Mention", "SmartHyperlink", "Hashtag", "UnresolvedMention", "User", "Nil"]  # noqa: E501
        if not style_identifier.isdigit():
            if style_identifier not in allowed_values:
                raise ValueError(
                    "Invalid value for `style_identifier` ({0}), must be one of {1}"  # noqa: E501
                    .format(style_identifier, allowed_values))
            self._style_identifier = style_identifier
        else:
            self._style_identifier = allowed_values[int(style_identifier) if six.PY3 else long(style_identifier)]

    @property
    def style_name(self):
        """Gets the style_name of this TableProperties.  # noqa: E501

        Gets or sets the name of the table style applied to this table.  # noqa: E501

        :return: The style_name of this TableProperties.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this TableProperties.

        Gets or sets the name of the table style applied to this table.  # noqa: E501

        :param style_name: The style_name of this TableProperties.  # noqa: E501
        :type: str
        """
        self._style_name = style_name

    @property
    def style_options(self):
        """Gets the style_options of this TableProperties.  # noqa: E501

        Gets or sets the bit flags, that specify how a table style is applied to this table.  # noqa: E501

        :return: The style_options of this TableProperties.  # noqa: E501
        :rtype: str
        """
        return self._style_options

    @style_options.setter
    def style_options(self, style_options):
        """Sets the style_options of this TableProperties.

        Gets or sets the bit flags, that specify how a table style is applied to this table.  # noqa: E501

        :param style_options: The style_options of this TableProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "FirstRow", "LastRow", "FirstColumn", "LastColumn", "RowBands", "Default", "ColumnBands", "Default2003"]  # noqa: E501
        if not style_options.isdigit():
            if style_options not in allowed_values:
                raise ValueError(
                    "Invalid value for `style_options` ({0}), must be one of {1}"  # noqa: E501
                    .format(style_options, allowed_values))
            self._style_options = style_options
        else:
            self._style_options = allowed_values[int(style_options) if six.PY3 else long(style_options)]

    @property
    def text_wrapping(self):
        """Gets the text_wrapping of this TableProperties.  # noqa: E501

        Gets or sets the option that controls text wrapping for the table.  # noqa: E501

        :return: The text_wrapping of this TableProperties.  # noqa: E501
        :rtype: str
        """
        return self._text_wrapping

    @text_wrapping.setter
    def text_wrapping(self, text_wrapping):
        """Sets the text_wrapping of this TableProperties.

        Gets or sets the option that controls text wrapping for the table.  # noqa: E501

        :param text_wrapping: The text_wrapping of this TableProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Default", "Around"]  # noqa: E501
        if not text_wrapping.isdigit():
            if text_wrapping not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_wrapping` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_wrapping, allowed_values))
            self._text_wrapping = text_wrapping
        else:
            self._text_wrapping = allowed_values[int(text_wrapping) if six.PY3 else long(text_wrapping)]

    @property
    def top_padding(self):
        """Gets the top_padding of this TableProperties.  # noqa: E501

        Gets or sets the amount of space (in points) to add above the contents of cells.  # noqa: E501

        :return: The top_padding of this TableProperties.  # noqa: E501
        :rtype: float
        """
        return self._top_padding

    @top_padding.setter
    def top_padding(self, top_padding):
        """Sets the top_padding of this TableProperties.

        Gets or sets the amount of space (in points) to add above the contents of cells.  # noqa: E501

        :param top_padding: The top_padding of this TableProperties.  # noqa: E501
        :type: float
        """
        self._top_padding = top_padding


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
        if not isinstance(other, TableProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other