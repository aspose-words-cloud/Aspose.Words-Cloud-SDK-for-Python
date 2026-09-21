# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="font.py">
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

class Font(object):
    """DTO container with a font element.
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
        'all_caps': 'bool',
        'bidi': 'bool',
        'bold': 'bool',
        'bold_bi': 'bool',
        'border': 'Border',
        'color': 'XmlColor',
        'complex_script': 'bool',
        'double_strike_through': 'bool',
        'emboss': 'bool',
        'engrave': 'bool',
        'hidden': 'bool',
        'highlight_color': 'XmlColor',
        'italic': 'bool',
        'italic_bi': 'bool',
        'kerning': 'float',
        'locale_id': 'int',
        'locale_id_bi': 'int',
        'locale_id_far_east': 'int',
        'name': 'str',
        'name_ascii': 'str',
        'name_bi': 'str',
        'name_far_east': 'str',
        'name_other': 'str',
        'no_proofing': 'bool',
        'outline': 'bool',
        'position': 'float',
        'scaling': 'int',
        'shadow': 'bool',
        'size': 'float',
        'size_bi': 'float',
        'small_caps': 'bool',
        'spacing': 'float',
        'strike_through': 'bool',
        'style_identifier': 'str',
        'style_name': 'str',
        'subscript': 'bool',
        'superscript': 'bool',
        'text_effect': 'str',
        'underline': 'str',
        'underline_color': 'XmlColor'
    }

    attribute_map = {
        'link': 'Link',
        'all_caps': 'AllCaps',
        'bidi': 'Bidi',
        'bold': 'Bold',
        'bold_bi': 'BoldBi',
        'border': 'Border',
        'color': 'Color',
        'complex_script': 'ComplexScript',
        'double_strike_through': 'DoubleStrikeThrough',
        'emboss': 'Emboss',
        'engrave': 'Engrave',
        'hidden': 'Hidden',
        'highlight_color': 'HighlightColor',
        'italic': 'Italic',
        'italic_bi': 'ItalicBi',
        'kerning': 'Kerning',
        'locale_id': 'LocaleId',
        'locale_id_bi': 'LocaleIdBi',
        'locale_id_far_east': 'LocaleIdFarEast',
        'name': 'Name',
        'name_ascii': 'NameAscii',
        'name_bi': 'NameBi',
        'name_far_east': 'NameFarEast',
        'name_other': 'NameOther',
        'no_proofing': 'NoProofing',
        'outline': 'Outline',
        'position': 'Position',
        'scaling': 'Scaling',
        'shadow': 'Shadow',
        'size': 'Size',
        'size_bi': 'SizeBi',
        'small_caps': 'SmallCaps',
        'spacing': 'Spacing',
        'strike_through': 'StrikeThrough',
        'style_identifier': 'StyleIdentifier',
        'style_name': 'StyleName',
        'subscript': 'Subscript',
        'superscript': 'Superscript',
        'text_effect': 'TextEffect',
        'underline': 'Underline',
        'underline_color': 'UnderlineColor'
    }

    def __init__(self, link=None, all_caps=None, bidi=None, bold=None, bold_bi=None, border=None, color=None, complex_script=None, double_strike_through=None, emboss=None, engrave=None, hidden=None, highlight_color=None, italic=None, italic_bi=None, kerning=None, locale_id=None, locale_id_bi=None, locale_id_far_east=None, name=None, name_ascii=None, name_bi=None, name_far_east=None, name_other=None, no_proofing=None, outline=None, position=None, scaling=None, shadow=None, size=None, size_bi=None, small_caps=None, spacing=None, strike_through=None, style_identifier=None, style_name=None, subscript=None, superscript=None, text_effect=None, underline=None, underline_color=None):  # noqa: E501
        """Font - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._all_caps = None
        self._bidi = None
        self._bold = None
        self._bold_bi = None
        self._border = None
        self._color = None
        self._complex_script = None
        self._double_strike_through = None
        self._emboss = None
        self._engrave = None
        self._hidden = None
        self._highlight_color = None
        self._italic = None
        self._italic_bi = None
        self._kerning = None
        self._locale_id = None
        self._locale_id_bi = None
        self._locale_id_far_east = None
        self._name = None
        self._name_ascii = None
        self._name_bi = None
        self._name_far_east = None
        self._name_other = None
        self._no_proofing = None
        self._outline = None
        self._position = None
        self._scaling = None
        self._shadow = None
        self._size = None
        self._size_bi = None
        self._small_caps = None
        self._spacing = None
        self._strike_through = None
        self._style_identifier = None
        self._style_name = None
        self._subscript = None
        self._superscript = None
        self._text_effect = None
        self._underline = None
        self._underline_color = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if all_caps is not None:
            self.all_caps = all_caps
        if bidi is not None:
            self.bidi = bidi
        if bold is not None:
            self.bold = bold
        if bold_bi is not None:
            self.bold_bi = bold_bi
        if border is not None:
            self.border = border
        if color is not None:
            self.color = color
        if complex_script is not None:
            self.complex_script = complex_script
        if double_strike_through is not None:
            self.double_strike_through = double_strike_through
        if emboss is not None:
            self.emboss = emboss
        if engrave is not None:
            self.engrave = engrave
        if hidden is not None:
            self.hidden = hidden
        if highlight_color is not None:
            self.highlight_color = highlight_color
        if italic is not None:
            self.italic = italic
        if italic_bi is not None:
            self.italic_bi = italic_bi
        if kerning is not None:
            self.kerning = kerning
        if locale_id is not None:
            self.locale_id = locale_id
        if locale_id_bi is not None:
            self.locale_id_bi = locale_id_bi
        if locale_id_far_east is not None:
            self.locale_id_far_east = locale_id_far_east
        if name is not None:
            self.name = name
        if name_ascii is not None:
            self.name_ascii = name_ascii
        if name_bi is not None:
            self.name_bi = name_bi
        if name_far_east is not None:
            self.name_far_east = name_far_east
        if name_other is not None:
            self.name_other = name_other
        if no_proofing is not None:
            self.no_proofing = no_proofing
        if outline is not None:
            self.outline = outline
        if position is not None:
            self.position = position
        if scaling is not None:
            self.scaling = scaling
        if shadow is not None:
            self.shadow = shadow
        if size is not None:
            self.size = size
        if size_bi is not None:
            self.size_bi = size_bi
        if small_caps is not None:
            self.small_caps = small_caps
        if spacing is not None:
            self.spacing = spacing
        if strike_through is not None:
            self.strike_through = strike_through
        if style_identifier is not None:
            self.style_identifier = style_identifier
        if style_name is not None:
            self.style_name = style_name
        if subscript is not None:
            self.subscript = subscript
        if superscript is not None:
            self.superscript = superscript
        if text_effect is not None:
            self.text_effect = text_effect
        if underline is not None:
            self.underline = underline
        if underline_color is not None:
            self.underline_color = underline_color

    @property
    def link(self):
        """Gets the link of this Font.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this Font.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Font.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this Font.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def all_caps(self):
        """Gets the all_caps of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as all capital letters.  # noqa: E501

        :return: The all_caps of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._all_caps

    @all_caps.setter
    def all_caps(self, all_caps):
        """Sets the all_caps of this Font.

        Gets or sets a value indicating whether the font is formatted as all capital letters.  # noqa: E501

        :param all_caps: The all_caps of this Font.  # noqa: E501
        :type: bool
        """
        self._all_caps = all_caps

    @property
    def bidi(self):
        """Gets the bidi of this Font.  # noqa: E501

        Gets or sets a value indicating whether the contents of this run shall have right-to-left characteristics. This property, when on, shall not be used with strongly left-to-right text. Any behavior under that condition is unspecified. This property, when off, shall not be used with strong right-to-left text. Any behavior under that condition is unspecified.When the contents of this run are displayed, all characters shall be treated as complex script characters for formatting purposes. This means that BoldBi, ItalicBi, SizeBi and a corresponding font name will be used when rendering this run.Also, when the contents of this run are displayed, this property acts as a right-to-left override for characters which are classified as "weak types" and "neutral types".  # noqa: E501

        :return: The bidi of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._bidi

    @bidi.setter
    def bidi(self, bidi):
        """Sets the bidi of this Font.

        Gets or sets a value indicating whether the contents of this run shall have right-to-left characteristics. This property, when on, shall not be used with strongly left-to-right text. Any behavior under that condition is unspecified. This property, when off, shall not be used with strong right-to-left text. Any behavior under that condition is unspecified.When the contents of this run are displayed, all characters shall be treated as complex script characters for formatting purposes. This means that BoldBi, ItalicBi, SizeBi and a corresponding font name will be used when rendering this run.Also, when the contents of this run are displayed, this property acts as a right-to-left override for characters which are classified as "weak types" and "neutral types".  # noqa: E501

        :param bidi: The bidi of this Font.  # noqa: E501
        :type: bool
        """
        self._bidi = bidi

    @property
    def bold(self):
        """Gets the bold of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as bold.  # noqa: E501

        :return: The bold of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this Font.

        Gets or sets a value indicating whether the font is formatted as bold.  # noqa: E501

        :param bold: The bold of this Font.  # noqa: E501
        :type: bool
        """
        self._bold = bold

    @property
    def bold_bi(self):
        """Gets the bold_bi of this Font.  # noqa: E501

        Gets or sets a value indicating whether the right-to-left text is formatted as bold.  # noqa: E501

        :return: The bold_bi of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._bold_bi

    @bold_bi.setter
    def bold_bi(self, bold_bi):
        """Sets the bold_bi of this Font.

        Gets or sets a value indicating whether the right-to-left text is formatted as bold.  # noqa: E501

        :param bold_bi: The bold_bi of this Font.  # noqa: E501
        :type: bool
        """
        self._bold_bi = bold_bi

    @property
    def border(self):
        """Gets the border of this Font.  # noqa: E501

        Gets or sets the border object, that specifies border for the font.  # noqa: E501

        :return: The border of this Font.  # noqa: E501
        :rtype: Border
        """
        return self._border

    @border.setter
    def border(self, border):
        """Sets the border of this Font.

        Gets or sets the border object, that specifies border for the font.  # noqa: E501

        :param border: The border of this Font.  # noqa: E501
        :type: Border
        """
        self._border = border

    @property
    def color(self):
        """Gets the color of this Font.  # noqa: E501

        Gets or sets the color of the font.  # noqa: E501

        :return: The color of this Font.  # noqa: E501
        :rtype: XmlColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Font.

        Gets or sets the color of the font.  # noqa: E501

        :param color: The color of this Font.  # noqa: E501
        :type: XmlColor
        """
        self._color = color

    @property
    def complex_script(self):
        """Gets the complex_script of this Font.  # noqa: E501

        Gets or sets a value indicating whether the contents of this run shall be treated as complex script text regardless of their Unicode character values when determining the formatting for this run.  # noqa: E501

        :return: The complex_script of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._complex_script

    @complex_script.setter
    def complex_script(self, complex_script):
        """Sets the complex_script of this Font.

        Gets or sets a value indicating whether the contents of this run shall be treated as complex script text regardless of their Unicode character values when determining the formatting for this run.  # noqa: E501

        :param complex_script: The complex_script of this Font.  # noqa: E501
        :type: bool
        """
        self._complex_script = complex_script

    @property
    def double_strike_through(self):
        """Gets the double_strike_through of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as double strikethrough text.  # noqa: E501

        :return: The double_strike_through of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._double_strike_through

    @double_strike_through.setter
    def double_strike_through(self, double_strike_through):
        """Sets the double_strike_through of this Font.

        Gets or sets a value indicating whether the font is formatted as double strikethrough text.  # noqa: E501

        :param double_strike_through: The double_strike_through of this Font.  # noqa: E501
        :type: bool
        """
        self._double_strike_through = double_strike_through

    @property
    def emboss(self):
        """Gets the emboss of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as embossed.  # noqa: E501

        :return: The emboss of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._emboss

    @emboss.setter
    def emboss(self, emboss):
        """Sets the emboss of this Font.

        Gets or sets a value indicating whether the font is formatted as embossed.  # noqa: E501

        :param emboss: The emboss of this Font.  # noqa: E501
        :type: bool
        """
        self._emboss = emboss

    @property
    def engrave(self):
        """Gets the engrave of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as engraved.  # noqa: E501

        :return: The engrave of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._engrave

    @engrave.setter
    def engrave(self, engrave):
        """Sets the engrave of this Font.

        Gets or sets a value indicating whether the font is formatted as engraved.  # noqa: E501

        :param engrave: The engrave of this Font.  # noqa: E501
        :type: bool
        """
        self._engrave = engrave

    @property
    def hidden(self):
        """Gets the hidden of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as hidden text.  # noqa: E501

        :return: The hidden of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Font.

        Gets or sets a value indicating whether the font is formatted as hidden text.  # noqa: E501

        :param hidden: The hidden of this Font.  # noqa: E501
        :type: bool
        """
        self._hidden = hidden

    @property
    def highlight_color(self):
        """Gets the highlight_color of this Font.  # noqa: E501

        Gets or sets the highlight (marker) color.  # noqa: E501

        :return: The highlight_color of this Font.  # noqa: E501
        :rtype: XmlColor
        """
        return self._highlight_color

    @highlight_color.setter
    def highlight_color(self, highlight_color):
        """Sets the highlight_color of this Font.

        Gets or sets the highlight (marker) color.  # noqa: E501

        :param highlight_color: The highlight_color of this Font.  # noqa: E501
        :type: XmlColor
        """
        self._highlight_color = highlight_color

    @property
    def italic(self):
        """Gets the italic of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as italic.  # noqa: E501

        :return: The italic of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """Sets the italic of this Font.

        Gets or sets a value indicating whether the font is formatted as italic.  # noqa: E501

        :param italic: The italic of this Font.  # noqa: E501
        :type: bool
        """
        self._italic = italic

    @property
    def italic_bi(self):
        """Gets the italic_bi of this Font.  # noqa: E501

        Gets or sets a value indicating whether the right-to-left text is formatted as italic.  # noqa: E501

        :return: The italic_bi of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._italic_bi

    @italic_bi.setter
    def italic_bi(self, italic_bi):
        """Sets the italic_bi of this Font.

        Gets or sets a value indicating whether the right-to-left text is formatted as italic.  # noqa: E501

        :param italic_bi: The italic_bi of this Font.  # noqa: E501
        :type: bool
        """
        self._italic_bi = italic_bi

    @property
    def kerning(self):
        """Gets the kerning of this Font.  # noqa: E501

        Gets or sets the font size at which kerning starts.  # noqa: E501

        :return: The kerning of this Font.  # noqa: E501
        :rtype: float
        """
        return self._kerning

    @kerning.setter
    def kerning(self, kerning):
        """Sets the kerning of this Font.

        Gets or sets the font size at which kerning starts.  # noqa: E501

        :param kerning: The kerning of this Font.  # noqa: E501
        :type: float
        """
        self._kerning = kerning

    @property
    def locale_id(self):
        """Gets the locale_id of this Font.  # noqa: E501

        Gets or sets the locale identifier (language) of the formatted characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :return: The locale_id of this Font.  # noqa: E501
        :rtype: int
        """
        return self._locale_id

    @locale_id.setter
    def locale_id(self, locale_id):
        """Sets the locale_id of this Font.

        Gets or sets the locale identifier (language) of the formatted characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :param locale_id: The locale_id of this Font.  # noqa: E501
        :type: int
        """
        self._locale_id = locale_id

    @property
    def locale_id_bi(self):
        """Gets the locale_id_bi of this Font.  # noqa: E501

        Gets or sets the locale identifier (language) of the formatted right-to-left characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :return: The locale_id_bi of this Font.  # noqa: E501
        :rtype: int
        """
        return self._locale_id_bi

    @locale_id_bi.setter
    def locale_id_bi(self, locale_id_bi):
        """Sets the locale_id_bi of this Font.

        Gets or sets the locale identifier (language) of the formatted right-to-left characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :param locale_id_bi: The locale_id_bi of this Font.  # noqa: E501
        :type: int
        """
        self._locale_id_bi = locale_id_bi

    @property
    def locale_id_far_east(self):
        """Gets the locale_id_far_east of this Font.  # noqa: E501

        Gets or sets the locale identifier (language) of the formatted Asian characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :return: The locale_id_far_east of this Font.  # noqa: E501
        :rtype: int
        """
        return self._locale_id_far_east

    @locale_id_far_east.setter
    def locale_id_far_east(self, locale_id_far_east):
        """Sets the locale_id_far_east of this Font.

        Gets or sets the locale identifier (language) of the formatted Asian characters. For the list of locale identifiers see http://www.microsoft.com/globaldev/reference/lcid-all.mspx.  # noqa: E501

        :param locale_id_far_east: The locale_id_far_east of this Font.  # noqa: E501
        :type: int
        """
        self._locale_id_far_east = locale_id_far_east

    @property
    def name(self):
        """Gets the name of this Font.  # noqa: E501

        Gets or sets the name of the font.  # noqa: E501

        :return: The name of this Font.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Font.

        Gets or sets the name of the font.  # noqa: E501

        :param name: The name of this Font.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def name_ascii(self):
        """Gets the name_ascii of this Font.  # noqa: E501

        Gets or sets the font used for Latin text (characters with character codes from 0 (zero) through 127).  # noqa: E501

        :return: The name_ascii of this Font.  # noqa: E501
        :rtype: str
        """
        return self._name_ascii

    @name_ascii.setter
    def name_ascii(self, name_ascii):
        """Sets the name_ascii of this Font.

        Gets or sets the font used for Latin text (characters with character codes from 0 (zero) through 127).  # noqa: E501

        :param name_ascii: The name_ascii of this Font.  # noqa: E501
        :type: str
        """
        self._name_ascii = name_ascii

    @property
    def name_bi(self):
        """Gets the name_bi of this Font.  # noqa: E501

        Gets or sets the name of the font in a right-to-left language document.  # noqa: E501

        :return: The name_bi of this Font.  # noqa: E501
        :rtype: str
        """
        return self._name_bi

    @name_bi.setter
    def name_bi(self, name_bi):
        """Sets the name_bi of this Font.

        Gets or sets the name of the font in a right-to-left language document.  # noqa: E501

        :param name_bi: The name_bi of this Font.  # noqa: E501
        :type: str
        """
        self._name_bi = name_bi

    @property
    def name_far_east(self):
        """Gets the name_far_east of this Font.  # noqa: E501

        Gets or sets the East Asian font name.  # noqa: E501

        :return: The name_far_east of this Font.  # noqa: E501
        :rtype: str
        """
        return self._name_far_east

    @name_far_east.setter
    def name_far_east(self, name_far_east):
        """Sets the name_far_east of this Font.

        Gets or sets the East Asian font name.  # noqa: E501

        :param name_far_east: The name_far_east of this Font.  # noqa: E501
        :type: str
        """
        self._name_far_east = name_far_east

    @property
    def name_other(self):
        """Gets the name_other of this Font.  # noqa: E501

        Gets or sets the font used for characters with character codes from 128 through 255.  # noqa: E501

        :return: The name_other of this Font.  # noqa: E501
        :rtype: str
        """
        return self._name_other

    @name_other.setter
    def name_other(self, name_other):
        """Sets the name_other of this Font.

        Gets or sets the font used for characters with character codes from 128 through 255.  # noqa: E501

        :param name_other: The name_other of this Font.  # noqa: E501
        :type: str
        """
        self._name_other = name_other

    @property
    def no_proofing(self):
        """Gets the no_proofing of this Font.  # noqa: E501

        Gets or sets a value indicating whether the formatted characters are not to be spell checked.  # noqa: E501

        :return: The no_proofing of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._no_proofing

    @no_proofing.setter
    def no_proofing(self, no_proofing):
        """Sets the no_proofing of this Font.

        Gets or sets a value indicating whether the formatted characters are not to be spell checked.  # noqa: E501

        :param no_proofing: The no_proofing of this Font.  # noqa: E501
        :type: bool
        """
        self._no_proofing = no_proofing

    @property
    def outline(self):
        """Gets the outline of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as outline.  # noqa: E501

        :return: The outline of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this Font.

        Gets or sets a value indicating whether the font is formatted as outline.  # noqa: E501

        :param outline: The outline of this Font.  # noqa: E501
        :type: bool
        """
        self._outline = outline

    @property
    def position(self):
        """Gets the position of this Font.  # noqa: E501

        Gets or sets the position of text (in points) relative to the base line. A positive number raises the text, and a negative number lowers it.  # noqa: E501

        :return: The position of this Font.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Font.

        Gets or sets the position of text (in points) relative to the base line. A positive number raises the text, and a negative number lowers it.  # noqa: E501

        :param position: The position of this Font.  # noqa: E501
        :type: float
        """
        self._position = position

    @property
    def scaling(self):
        """Gets the scaling of this Font.  # noqa: E501

        Gets or sets character width scaling in percent.  # noqa: E501

        :return: The scaling of this Font.  # noqa: E501
        :rtype: int
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        """Sets the scaling of this Font.

        Gets or sets character width scaling in percent.  # noqa: E501

        :param scaling: The scaling of this Font.  # noqa: E501
        :type: int
        """
        self._scaling = scaling

    @property
    def shadow(self):
        """Gets the shadow of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as shadowed.  # noqa: E501

        :return: The shadow of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._shadow

    @shadow.setter
    def shadow(self, shadow):
        """Sets the shadow of this Font.

        Gets or sets a value indicating whether the font is formatted as shadowed.  # noqa: E501

        :param shadow: The shadow of this Font.  # noqa: E501
        :type: bool
        """
        self._shadow = shadow

    @property
    def size(self):
        """Gets the size of this Font.  # noqa: E501

        Gets or sets the font size in points.  # noqa: E501

        :return: The size of this Font.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Font.

        Gets or sets the font size in points.  # noqa: E501

        :param size: The size of this Font.  # noqa: E501
        :type: float
        """
        self._size = size

    @property
    def size_bi(self):
        """Gets the size_bi of this Font.  # noqa: E501

        Gets or sets the font size in points used in a right-to-left document.  # noqa: E501

        :return: The size_bi of this Font.  # noqa: E501
        :rtype: float
        """
        return self._size_bi

    @size_bi.setter
    def size_bi(self, size_bi):
        """Sets the size_bi of this Font.

        Gets or sets the font size in points used in a right-to-left document.  # noqa: E501

        :param size_bi: The size_bi of this Font.  # noqa: E501
        :type: float
        """
        self._size_bi = size_bi

    @property
    def small_caps(self):
        """Gets the small_caps of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as small capital letters.  # noqa: E501

        :return: The small_caps of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._small_caps

    @small_caps.setter
    def small_caps(self, small_caps):
        """Sets the small_caps of this Font.

        Gets or sets a value indicating whether the font is formatted as small capital letters.  # noqa: E501

        :param small_caps: The small_caps of this Font.  # noqa: E501
        :type: bool
        """
        self._small_caps = small_caps

    @property
    def spacing(self):
        """Gets the spacing of this Font.  # noqa: E501

        Gets or sets the spacing (in points) between characters.  # noqa: E501

        :return: The spacing of this Font.  # noqa: E501
        :rtype: float
        """
        return self._spacing

    @spacing.setter
    def spacing(self, spacing):
        """Sets the spacing of this Font.

        Gets or sets the spacing (in points) between characters.  # noqa: E501

        :param spacing: The spacing of this Font.  # noqa: E501
        :type: float
        """
        self._spacing = spacing

    @property
    def strike_through(self):
        """Gets the strike_through of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as strikethrough text.  # noqa: E501

        :return: The strike_through of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._strike_through

    @strike_through.setter
    def strike_through(self, strike_through):
        """Sets the strike_through of this Font.

        Gets or sets a value indicating whether the font is formatted as strikethrough text.  # noqa: E501

        :param strike_through: The strike_through of this Font.  # noqa: E501
        :type: bool
        """
        self._strike_through = strike_through

    @property
    def style_identifier(self):
        """Gets the style_identifier of this Font.  # noqa: E501

        Gets or sets the locale independent style identifier of the character style applied to this formatting.  # noqa: E501

        :return: The style_identifier of this Font.  # noqa: E501
        :rtype: str
        """
        return self._style_identifier

    @style_identifier.setter
    def style_identifier(self, style_identifier):
        """Sets the style_identifier of this Font.

        Gets or sets the locale independent style identifier of the character style applied to this formatting.  # noqa: E501

        :param style_identifier: The style_identifier of this Font.  # noqa: E501
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
        """Gets the style_name of this Font.  # noqa: E501

        Gets or sets the name of the character style applied to this formatting.  # noqa: E501

        :return: The style_name of this Font.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this Font.

        Gets or sets the name of the character style applied to this formatting.  # noqa: E501

        :param style_name: The style_name of this Font.  # noqa: E501
        :type: str
        """
        self._style_name = style_name

    @property
    def subscript(self):
        """Gets the subscript of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as subscript.  # noqa: E501

        :return: The subscript of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._subscript

    @subscript.setter
    def subscript(self, subscript):
        """Sets the subscript of this Font.

        Gets or sets a value indicating whether the font is formatted as subscript.  # noqa: E501

        :param subscript: The subscript of this Font.  # noqa: E501
        :type: bool
        """
        self._subscript = subscript

    @property
    def superscript(self):
        """Gets the superscript of this Font.  # noqa: E501

        Gets or sets a value indicating whether the font is formatted as superscript.  # noqa: E501

        :return: The superscript of this Font.  # noqa: E501
        :rtype: bool
        """
        return self._superscript

    @superscript.setter
    def superscript(self, superscript):
        """Sets the superscript of this Font.

        Gets or sets a value indicating whether the font is formatted as superscript.  # noqa: E501

        :param superscript: The superscript of this Font.  # noqa: E501
        :type: bool
        """
        self._superscript = superscript

    @property
    def text_effect(self):
        """Gets the text_effect of this Font.  # noqa: E501

        Gets or sets the font animation effect.  # noqa: E501

        :return: The text_effect of this Font.  # noqa: E501
        :rtype: str
        """
        return self._text_effect

    @text_effect.setter
    def text_effect(self, text_effect):
        """Sets the text_effect of this Font.

        Gets or sets the font animation effect.  # noqa: E501

        :param text_effect: The text_effect of this Font.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "LasVegasLights", "BlinkingBackground", "SparkleText", "MarchingBlackAnts", "MarchingRedAnts", "Shimmer"]  # noqa: E501
        if not text_effect.isdigit():
            if text_effect not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_effect` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_effect, allowed_values))
            self._text_effect = text_effect
        else:
            self._text_effect = allowed_values[int(text_effect) if six.PY3 else long(text_effect)]

    @property
    def underline(self):
        """Gets the underline of this Font.  # noqa: E501

        Gets or sets the type of underline applied to the font.  # noqa: E501

        :return: The underline of this Font.  # noqa: E501
        :rtype: str
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """Sets the underline of this Font.

        Gets or sets the type of underline applied to the font.  # noqa: E501

        :param underline: The underline of this Font.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Single", "Words", "Double", "Dotted", "Thick", "Dash", "DotDash", "DotDotDash", "Wavy", "DottedHeavy", "DashHeavy", "DotDashHeavy", "DotDotDashHeavy", "WavyHeavy", "DashLong", "WavyDouble", "DashLongHeavy"]  # noqa: E501
        if not underline.isdigit():
            if underline not in allowed_values:
                raise ValueError(
                    "Invalid value for `underline` ({0}), must be one of {1}"  # noqa: E501
                    .format(underline, allowed_values))
            self._underline = underline
        else:
            self._underline = allowed_values[int(underline) if six.PY3 else long(underline)]

    @property
    def underline_color(self):
        """Gets the underline_color of this Font.  # noqa: E501

        Gets or sets the color of the underline applied to the font.  # noqa: E501

        :return: The underline_color of this Font.  # noqa: E501
        :rtype: XmlColor
        """
        return self._underline_color

    @underline_color.setter
    def underline_color(self, underline_color):
        """Sets the underline_color of this Font.

        Gets or sets the color of the underline applied to the font.  # noqa: E501

        :param underline_color: The underline_color of this Font.  # noqa: E501
        :type: XmlColor
        """
        self._underline_color = underline_color


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()







        if self._border is not None:
            self._border.validate()



        if self._color is not None:
            self._color.validate()








        if self._highlight_color is not None:
            self._highlight_color.validate()






























        if self._underline_color is not None:
            self._underline_color.validate()


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
        if not isinstance(other, Font):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other