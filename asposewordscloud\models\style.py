# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="style.py">
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

class Style(object):
    """DTO container with a single document style.
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
        'font': 'Font',
        'built_in': 'bool',
        'next_paragraph_style_name': 'str',
        'base_style_name': 'str',
        'is_quick_style': 'bool',
        'linked_style_name': 'str',
        'type': 'str',
        'is_heading': 'bool',
        'aliases': 'list[str]',
        'style_identifier': 'str',
        'name': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'font': 'Font',
        'built_in': 'BuiltIn',
        'next_paragraph_style_name': 'NextParagraphStyleName',
        'base_style_name': 'BaseStyleName',
        'is_quick_style': 'IsQuickStyle',
        'linked_style_name': 'LinkedStyleName',
        'type': 'Type',
        'is_heading': 'IsHeading',
        'aliases': 'Aliases',
        'style_identifier': 'StyleIdentifier',
        'name': 'Name'
    }

    def __init__(self, link=None, font=None, built_in=None, next_paragraph_style_name=None, base_style_name=None, is_quick_style=None, linked_style_name=None, type=None, is_heading=None, aliases=None, style_identifier=None, name=None):  # noqa: E501
        """Style - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._font = None
        self._built_in = None
        self._next_paragraph_style_name = None
        self._base_style_name = None
        self._is_quick_style = None
        self._linked_style_name = None
        self._type = None
        self._is_heading = None
        self._aliases = None
        self._style_identifier = None
        self._name = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if font is not None:
            self.font = font
        if built_in is not None:
            self.built_in = built_in
        if next_paragraph_style_name is not None:
            self.next_paragraph_style_name = next_paragraph_style_name
        if base_style_name is not None:
            self.base_style_name = base_style_name
        if is_quick_style is not None:
            self.is_quick_style = is_quick_style
        if linked_style_name is not None:
            self.linked_style_name = linked_style_name
        if type is not None:
            self.type = type
        if is_heading is not None:
            self.is_heading = is_heading
        if aliases is not None:
            self.aliases = aliases
        if style_identifier is not None:
            self.style_identifier = style_identifier
        if name is not None:
            self.name = name

    @property
    def link(self):
        """Gets the link of this Style.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this Style.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Style.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this Style.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def font(self):
        """Gets the font of this Style.  # noqa: E501

        Gets or sets the character formatting of the style. For list styles this property returns null.  # noqa: E501

        :return: The font of this Style.  # noqa: E501
        :rtype: Font
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this Style.

        Gets or sets the character formatting of the style. For list styles this property returns null.  # noqa: E501

        :param font: The font of this Style.  # noqa: E501
        :type: Font
        """
        self._font = font

    @property
    def built_in(self):
        """Gets the built_in of this Style.  # noqa: E501

        Gets or sets a value indicating whether this style is one of the built-in styles in MS Word.  # noqa: E501

        :return: The built_in of this Style.  # noqa: E501
        :rtype: bool
        """
        return self._built_in

    @built_in.setter
    def built_in(self, built_in):
        """Sets the built_in of this Style.

        Gets or sets a value indicating whether this style is one of the built-in styles in MS Word.  # noqa: E501

        :param built_in: The built_in of this Style.  # noqa: E501
        :type: bool
        """
        self._built_in = built_in

    @property
    def next_paragraph_style_name(self):
        """Gets the next_paragraph_style_name of this Style.  # noqa: E501

        Gets or sets the name of the style to be applied automatically to a new paragraph inserted after a paragraph formatted with the specified style. This property is not used by Aspose.Words. The next paragraph style will only be applied automatically when you edit the document in MS Word.  # noqa: E501

        :return: The next_paragraph_style_name of this Style.  # noqa: E501
        :rtype: str
        """
        return self._next_paragraph_style_name

    @next_paragraph_style_name.setter
    def next_paragraph_style_name(self, next_paragraph_style_name):
        """Sets the next_paragraph_style_name of this Style.

        Gets or sets the name of the style to be applied automatically to a new paragraph inserted after a paragraph formatted with the specified style. This property is not used by Aspose.Words. The next paragraph style will only be applied automatically when you edit the document in MS Word.  # noqa: E501

        :param next_paragraph_style_name: The next_paragraph_style_name of this Style.  # noqa: E501
        :type: str
        """
        self._next_paragraph_style_name = next_paragraph_style_name

    @property
    def base_style_name(self):
        """Gets the base_style_name of this Style.  # noqa: E501

        Gets or sets the name of the style this style is based on. This will be an empty string if the style is not based on any other style and it can be set to an empty string.  # noqa: E501

        :return: The base_style_name of this Style.  # noqa: E501
        :rtype: str
        """
        return self._base_style_name

    @base_style_name.setter
    def base_style_name(self, base_style_name):
        """Sets the base_style_name of this Style.

        Gets or sets the name of the style this style is based on. This will be an empty string if the style is not based on any other style and it can be set to an empty string.  # noqa: E501

        :param base_style_name: The base_style_name of this Style.  # noqa: E501
        :type: str
        """
        self._base_style_name = base_style_name

    @property
    def is_quick_style(self):
        """Gets the is_quick_style of this Style.  # noqa: E501

        Gets or sets a value indicating whether this style is shown in the Quick Style gallery inside MS Word UI.  # noqa: E501

        :return: The is_quick_style of this Style.  # noqa: E501
        :rtype: bool
        """
        return self._is_quick_style

    @is_quick_style.setter
    def is_quick_style(self, is_quick_style):
        """Sets the is_quick_style of this Style.

        Gets or sets a value indicating whether this style is shown in the Quick Style gallery inside MS Word UI.  # noqa: E501

        :param is_quick_style: The is_quick_style of this Style.  # noqa: E501
        :type: bool
        """
        self._is_quick_style = is_quick_style

    @property
    def linked_style_name(self):
        """Gets the linked_style_name of this Style.  # noqa: E501

        Gets or sets the name of the Style linked to this one. Returns Empty string if no styles are linked.  # noqa: E501

        :return: The linked_style_name of this Style.  # noqa: E501
        :rtype: str
        """
        return self._linked_style_name

    @linked_style_name.setter
    def linked_style_name(self, linked_style_name):
        """Sets the linked_style_name of this Style.

        Gets or sets the name of the Style linked to this one. Returns Empty string if no styles are linked.  # noqa: E501

        :param linked_style_name: The linked_style_name of this Style.  # noqa: E501
        :type: str
        """
        self._linked_style_name = linked_style_name

    @property
    def type(self):
        """Gets the type of this Style.  # noqa: E501

        Gets or sets the style type (paragraph or character).  # noqa: E501

        :return: The type of this Style.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Style.

        Gets or sets the style type (paragraph or character).  # noqa: E501

        :param type: The type of this Style.  # noqa: E501
        :type: str
        """
        allowed_values = ["Paragraph", "Character", "Table", "List"]  # noqa: E501
        if not type.isdigit():
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values))
            self._type = type
        else:
            self._type = allowed_values[int(type) if six.PY3 else long(type)]

    @property
    def is_heading(self):
        """Gets the is_heading of this Style.  # noqa: E501

        Gets or sets a value indicating whether the style is one of the built-in Heading styles.  # noqa: E501

        :return: The is_heading of this Style.  # noqa: E501
        :rtype: bool
        """
        return self._is_heading

    @is_heading.setter
    def is_heading(self, is_heading):
        """Sets the is_heading of this Style.

        Gets or sets a value indicating whether the style is one of the built-in Heading styles.  # noqa: E501

        :param is_heading: The is_heading of this Style.  # noqa: E501
        :type: bool
        """
        self._is_heading = is_heading

    @property
    def aliases(self):
        """Gets the aliases of this Style.  # noqa: E501

        Gets or sets all aliases of this style. If style has no aliases then empty array of string is returned.  # noqa: E501

        :return: The aliases of this Style.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Style.

        Gets or sets all aliases of this style. If style has no aliases then empty array of string is returned.  # noqa: E501

        :param aliases: The aliases of this Style.  # noqa: E501
        :type: list[str]
        """
        self._aliases = aliases

    @property
    def style_identifier(self):
        """Gets the style_identifier of this Style.  # noqa: E501

        Gets or sets the locale independent style identifier for a built-in style. For user defined (custom) styles, this property returns Aspose.Words.StyleIdentifier.User. Aspose.Words.Style.Name.  # noqa: E501

        :return: The style_identifier of this Style.  # noqa: E501
        :rtype: str
        """
        return self._style_identifier

    @style_identifier.setter
    def style_identifier(self, style_identifier):
        """Sets the style_identifier of this Style.

        Gets or sets the locale independent style identifier for a built-in style. For user defined (custom) styles, this property returns Aspose.Words.StyleIdentifier.User. Aspose.Words.Style.Name.  # noqa: E501

        :param style_identifier: The style_identifier of this Style.  # noqa: E501
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
    def name(self):
        """Gets the name of this Style.  # noqa: E501

        Gets or sets the name of the style. Cannot be an empty string. If there already is a style with such name in the collection, then this style will override it. All affected nodes will reference new style.  # noqa: E501

        :return: The name of this Style.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Style.

        Gets or sets the name of the style. Cannot be an empty string. If there already is a style with such name in the collection, then this style will override it. All affected nodes will reference new style.  # noqa: E501

        :param name: The name of this Style.  # noqa: E501
        :type: str
        """
        self._name = name


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._built_in is None:
            raise ValueError("Property BuiltIn in Style is required.")  # noqa: E501
        if self._is_quick_style is None:
            raise ValueError("Property IsQuickStyle in Style is required.")  # noqa: E501
        if self._type is None:
            raise ValueError("Property Type in Style is required.")  # noqa: E501
        if self._is_heading is None:
            raise ValueError("Property IsHeading in Style is required.")  # noqa: E501
        if self._style_identifier is None:
            raise ValueError("Property StyleIdentifier in Style is required.")  # noqa: E501

        if self._link is not None:
            self._link.validate()



        if self._font is not None:
            self._font.validate()












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
        if not isinstance(other, Style):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other