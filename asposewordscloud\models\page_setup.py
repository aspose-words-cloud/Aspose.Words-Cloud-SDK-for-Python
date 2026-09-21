# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="page_setup.py">
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

class PageSetup(object):
    """Represents the page setup properties of a section. PageSetup object contains all the page setup attributes of a section (left margin, bottom margin, paper size, and so on) as properties.
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
        'bidi': 'bool',
        'border_always_in_front': 'bool',
        'border_applies_to': 'str',
        'border_distance_from': 'str',
        'bottom_margin': 'float',
        'different_first_page_header_footer': 'bool',
        'first_page_tray': 'int',
        'footer_distance': 'float',
        'gutter': 'float',
        'header_distance': 'float',
        'left_margin': 'float',
        'line_number_count_by': 'int',
        'line_number_distance_from_text': 'float',
        'line_number_restart_mode': 'str',
        'line_starting_number': 'int',
        'orientation': 'str',
        'other_pages_tray': 'int',
        'page_height': 'float',
        'page_number_style': 'str',
        'page_starting_number': 'int',
        'page_width': 'float',
        'paper_size': 'str',
        'restart_page_numbering': 'bool',
        'right_margin': 'float',
        'rtl_gutter': 'bool',
        'section_start': 'str',
        'suppress_endnotes': 'bool',
        'top_margin': 'float',
        'vertical_alignment': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'bidi': 'Bidi',
        'border_always_in_front': 'BorderAlwaysInFront',
        'border_applies_to': 'BorderAppliesTo',
        'border_distance_from': 'BorderDistanceFrom',
        'bottom_margin': 'BottomMargin',
        'different_first_page_header_footer': 'DifferentFirstPageHeaderFooter',
        'first_page_tray': 'FirstPageTray',
        'footer_distance': 'FooterDistance',
        'gutter': 'Gutter',
        'header_distance': 'HeaderDistance',
        'left_margin': 'LeftMargin',
        'line_number_count_by': 'LineNumberCountBy',
        'line_number_distance_from_text': 'LineNumberDistanceFromText',
        'line_number_restart_mode': 'LineNumberRestartMode',
        'line_starting_number': 'LineStartingNumber',
        'orientation': 'Orientation',
        'other_pages_tray': 'OtherPagesTray',
        'page_height': 'PageHeight',
        'page_number_style': 'PageNumberStyle',
        'page_starting_number': 'PageStartingNumber',
        'page_width': 'PageWidth',
        'paper_size': 'PaperSize',
        'restart_page_numbering': 'RestartPageNumbering',
        'right_margin': 'RightMargin',
        'rtl_gutter': 'RtlGutter',
        'section_start': 'SectionStart',
        'suppress_endnotes': 'SuppressEndnotes',
        'top_margin': 'TopMargin',
        'vertical_alignment': 'VerticalAlignment'
    }

    def __init__(self, link=None, bidi=None, border_always_in_front=None, border_applies_to=None, border_distance_from=None, bottom_margin=None, different_first_page_header_footer=None, first_page_tray=None, footer_distance=None, gutter=None, header_distance=None, left_margin=None, line_number_count_by=None, line_number_distance_from_text=None, line_number_restart_mode=None, line_starting_number=None, orientation=None, other_pages_tray=None, page_height=None, page_number_style=None, page_starting_number=None, page_width=None, paper_size=None, restart_page_numbering=None, right_margin=None, rtl_gutter=None, section_start=None, suppress_endnotes=None, top_margin=None, vertical_alignment=None):  # noqa: E501
        """PageSetup - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._bidi = None
        self._border_always_in_front = None
        self._border_applies_to = None
        self._border_distance_from = None
        self._bottom_margin = None
        self._different_first_page_header_footer = None
        self._first_page_tray = None
        self._footer_distance = None
        self._gutter = None
        self._header_distance = None
        self._left_margin = None
        self._line_number_count_by = None
        self._line_number_distance_from_text = None
        self._line_number_restart_mode = None
        self._line_starting_number = None
        self._orientation = None
        self._other_pages_tray = None
        self._page_height = None
        self._page_number_style = None
        self._page_starting_number = None
        self._page_width = None
        self._paper_size = None
        self._restart_page_numbering = None
        self._right_margin = None
        self._rtl_gutter = None
        self._section_start = None
        self._suppress_endnotes = None
        self._top_margin = None
        self._vertical_alignment = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if bidi is not None:
            self.bidi = bidi
        if border_always_in_front is not None:
            self.border_always_in_front = border_always_in_front
        if border_applies_to is not None:
            self.border_applies_to = border_applies_to
        if border_distance_from is not None:
            self.border_distance_from = border_distance_from
        if bottom_margin is not None:
            self.bottom_margin = bottom_margin
        if different_first_page_header_footer is not None:
            self.different_first_page_header_footer = different_first_page_header_footer
        if first_page_tray is not None:
            self.first_page_tray = first_page_tray
        if footer_distance is not None:
            self.footer_distance = footer_distance
        if gutter is not None:
            self.gutter = gutter
        if header_distance is not None:
            self.header_distance = header_distance
        if left_margin is not None:
            self.left_margin = left_margin
        if line_number_count_by is not None:
            self.line_number_count_by = line_number_count_by
        if line_number_distance_from_text is not None:
            self.line_number_distance_from_text = line_number_distance_from_text
        if line_number_restart_mode is not None:
            self.line_number_restart_mode = line_number_restart_mode
        if line_starting_number is not None:
            self.line_starting_number = line_starting_number
        if orientation is not None:
            self.orientation = orientation
        if other_pages_tray is not None:
            self.other_pages_tray = other_pages_tray
        if page_height is not None:
            self.page_height = page_height
        if page_number_style is not None:
            self.page_number_style = page_number_style
        if page_starting_number is not None:
            self.page_starting_number = page_starting_number
        if page_width is not None:
            self.page_width = page_width
        if paper_size is not None:
            self.paper_size = paper_size
        if restart_page_numbering is not None:
            self.restart_page_numbering = restart_page_numbering
        if right_margin is not None:
            self.right_margin = right_margin
        if rtl_gutter is not None:
            self.rtl_gutter = rtl_gutter
        if section_start is not None:
            self.section_start = section_start
        if suppress_endnotes is not None:
            self.suppress_endnotes = suppress_endnotes
        if top_margin is not None:
            self.top_margin = top_margin
        if vertical_alignment is not None:
            self.vertical_alignment = vertical_alignment

    @property
    def link(self):
        """Gets the link of this PageSetup.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this PageSetup.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this PageSetup.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this PageSetup.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def bidi(self):
        """Gets the bidi of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether this section contains bidirectional (complex scripts) text. When true, the columns in this section are laid out from right to left.  # noqa: E501

        :return: The bidi of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._bidi

    @bidi.setter
    def bidi(self, bidi):
        """Sets the bidi of this PageSetup.

        Gets or sets a value indicating whether this section contains bidirectional (complex scripts) text. When true, the columns in this section are laid out from right to left.  # noqa: E501

        :param bidi: The bidi of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._bidi = bidi

    @property
    def border_always_in_front(self):
        """Gets the border_always_in_front of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether the page border is positioned relative to intersecting texts and objects.  # noqa: E501

        :return: The border_always_in_front of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._border_always_in_front

    @border_always_in_front.setter
    def border_always_in_front(self, border_always_in_front):
        """Sets the border_always_in_front of this PageSetup.

        Gets or sets a value indicating whether the page border is positioned relative to intersecting texts and objects.  # noqa: E501

        :param border_always_in_front: The border_always_in_front of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._border_always_in_front = border_always_in_front

    @property
    def border_applies_to(self):
        """Gets the border_applies_to of this PageSetup.  # noqa: E501

        Gets or sets the option that controls which pages the page border is printed on.  # noqa: E501

        :return: The border_applies_to of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._border_applies_to

    @border_applies_to.setter
    def border_applies_to(self, border_applies_to):
        """Sets the border_applies_to of this PageSetup.

        Gets or sets the option that controls which pages the page border is printed on.  # noqa: E501

        :param border_applies_to: The border_applies_to of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["AllPages", "FirstPage", "OtherPages"]  # noqa: E501
        if not border_applies_to.isdigit():
            if border_applies_to not in allowed_values:
                raise ValueError(
                    "Invalid value for `border_applies_to` ({0}), must be one of {1}"  # noqa: E501
                    .format(border_applies_to, allowed_values))
            self._border_applies_to = border_applies_to
        else:
            self._border_applies_to = allowed_values[int(border_applies_to) if six.PY3 else long(border_applies_to)]

    @property
    def border_distance_from(self):
        """Gets the border_distance_from of this PageSetup.  # noqa: E501

        Gets or sets the value, that indicates whether the specified page border is measured from the edge of the page or from the text it surrounds.  # noqa: E501

        :return: The border_distance_from of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._border_distance_from

    @border_distance_from.setter
    def border_distance_from(self, border_distance_from):
        """Sets the border_distance_from of this PageSetup.

        Gets or sets the value, that indicates whether the specified page border is measured from the edge of the page or from the text it surrounds.  # noqa: E501

        :param border_distance_from: The border_distance_from of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["Text", "PageEdge"]  # noqa: E501
        if not border_distance_from.isdigit():
            if border_distance_from not in allowed_values:
                raise ValueError(
                    "Invalid value for `border_distance_from` ({0}), must be one of {1}"  # noqa: E501
                    .format(border_distance_from, allowed_values))
            self._border_distance_from = border_distance_from
        else:
            self._border_distance_from = allowed_values[int(border_distance_from) if six.PY3 else long(border_distance_from)]

    @property
    def bottom_margin(self):
        """Gets the bottom_margin of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the bottom edge of the page and the bottom boundary of the body text.  # noqa: E501

        :return: The bottom_margin of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """Sets the bottom_margin of this PageSetup.

        Gets or sets the distance (in points) between the bottom edge of the page and the bottom boundary of the body text.  # noqa: E501

        :param bottom_margin: The bottom_margin of this PageSetup.  # noqa: E501
        :type: float
        """
        self._bottom_margin = bottom_margin

    @property
    def different_first_page_header_footer(self):
        """Gets the different_first_page_header_footer of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether a different header or footer is used on the first page.  # noqa: E501

        :return: The different_first_page_header_footer of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._different_first_page_header_footer

    @different_first_page_header_footer.setter
    def different_first_page_header_footer(self, different_first_page_header_footer):
        """Sets the different_first_page_header_footer of this PageSetup.

        Gets or sets a value indicating whether a different header or footer is used on the first page.  # noqa: E501

        :param different_first_page_header_footer: The different_first_page_header_footer of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._different_first_page_header_footer = different_first_page_header_footer

    @property
    def first_page_tray(self):
        """Gets the first_page_tray of this PageSetup.  # noqa: E501

        Gets or sets the paper tray (bin) to use for the first page of a section. The value is implementation (printer) specific.  # noqa: E501

        :return: The first_page_tray of this PageSetup.  # noqa: E501
        :rtype: int
        """
        return self._first_page_tray

    @first_page_tray.setter
    def first_page_tray(self, first_page_tray):
        """Sets the first_page_tray of this PageSetup.

        Gets or sets the paper tray (bin) to use for the first page of a section. The value is implementation (printer) specific.  # noqa: E501

        :param first_page_tray: The first_page_tray of this PageSetup.  # noqa: E501
        :type: int
        """
        self._first_page_tray = first_page_tray

    @property
    def footer_distance(self):
        """Gets the footer_distance of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the footer and the bottom of the page.  # noqa: E501

        :return: The footer_distance of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._footer_distance

    @footer_distance.setter
    def footer_distance(self, footer_distance):
        """Sets the footer_distance of this PageSetup.

        Gets or sets the distance (in points) between the footer and the bottom of the page.  # noqa: E501

        :param footer_distance: The footer_distance of this PageSetup.  # noqa: E501
        :type: float
        """
        self._footer_distance = footer_distance

    @property
    def gutter(self):
        """Gets the gutter of this PageSetup.  # noqa: E501

        Gets or sets the amount of extra space added to the margin for document binding.  # noqa: E501

        :return: The gutter of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._gutter

    @gutter.setter
    def gutter(self, gutter):
        """Sets the gutter of this PageSetup.

        Gets or sets the amount of extra space added to the margin for document binding.  # noqa: E501

        :param gutter: The gutter of this PageSetup.  # noqa: E501
        :type: float
        """
        self._gutter = gutter

    @property
    def header_distance(self):
        """Gets the header_distance of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the header and the top of the page.  # noqa: E501

        :return: The header_distance of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._header_distance

    @header_distance.setter
    def header_distance(self, header_distance):
        """Sets the header_distance of this PageSetup.

        Gets or sets the distance (in points) between the header and the top of the page.  # noqa: E501

        :param header_distance: The header_distance of this PageSetup.  # noqa: E501
        :type: float
        """
        self._header_distance = header_distance

    @property
    def left_margin(self):
        """Gets the left_margin of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the left edge of the page and the left boundary of the body text.  # noqa: E501

        :return: The left_margin of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """Sets the left_margin of this PageSetup.

        Gets or sets the distance (in points) between the left edge of the page and the left boundary of the body text.  # noqa: E501

        :param left_margin: The left_margin of this PageSetup.  # noqa: E501
        :type: float
        """
        self._left_margin = left_margin

    @property
    def line_number_count_by(self):
        """Gets the line_number_count_by of this PageSetup.  # noqa: E501

        Gets or sets the numeric increment for line numbers.  # noqa: E501

        :return: The line_number_count_by of this PageSetup.  # noqa: E501
        :rtype: int
        """
        return self._line_number_count_by

    @line_number_count_by.setter
    def line_number_count_by(self, line_number_count_by):
        """Sets the line_number_count_by of this PageSetup.

        Gets or sets the numeric increment for line numbers.  # noqa: E501

        :param line_number_count_by: The line_number_count_by of this PageSetup.  # noqa: E501
        :type: int
        """
        self._line_number_count_by = line_number_count_by

    @property
    def line_number_distance_from_text(self):
        """Gets the line_number_distance_from_text of this PageSetup.  # noqa: E501

        Gets or sets the distance between the right edge of line numbers and the left edge of the document. Set this property to zero for automatic distance between the line numbers and text of the document.  # noqa: E501

        :return: The line_number_distance_from_text of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._line_number_distance_from_text

    @line_number_distance_from_text.setter
    def line_number_distance_from_text(self, line_number_distance_from_text):
        """Sets the line_number_distance_from_text of this PageSetup.

        Gets or sets the distance between the right edge of line numbers and the left edge of the document. Set this property to zero for automatic distance between the line numbers and text of the document.  # noqa: E501

        :param line_number_distance_from_text: The line_number_distance_from_text of this PageSetup.  # noqa: E501
        :type: float
        """
        self._line_number_distance_from_text = line_number_distance_from_text

    @property
    def line_number_restart_mode(self):
        """Gets the line_number_restart_mode of this PageSetup.  # noqa: E501

        Gets or sets the way line numbering runs  that is, whether it starts over at the beginning of a new page or section or runs continuously.  # noqa: E501

        :return: The line_number_restart_mode of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._line_number_restart_mode

    @line_number_restart_mode.setter
    def line_number_restart_mode(self, line_number_restart_mode):
        """Sets the line_number_restart_mode of this PageSetup.

        Gets or sets the way line numbering runs  that is, whether it starts over at the beginning of a new page or section or runs continuously.  # noqa: E501

        :param line_number_restart_mode: The line_number_restart_mode of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["RestartPage", "RestartSection", "Continuous"]  # noqa: E501
        if not line_number_restart_mode.isdigit():
            if line_number_restart_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `line_number_restart_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(line_number_restart_mode, allowed_values))
            self._line_number_restart_mode = line_number_restart_mode
        else:
            self._line_number_restart_mode = allowed_values[int(line_number_restart_mode) if six.PY3 else long(line_number_restart_mode)]

    @property
    def line_starting_number(self):
        """Gets the line_starting_number of this PageSetup.  # noqa: E501

        Gets or sets the starting line number.  # noqa: E501

        :return: The line_starting_number of this PageSetup.  # noqa: E501
        :rtype: int
        """
        return self._line_starting_number

    @line_starting_number.setter
    def line_starting_number(self, line_starting_number):
        """Sets the line_starting_number of this PageSetup.

        Gets or sets the starting line number.  # noqa: E501

        :param line_starting_number: The line_starting_number of this PageSetup.  # noqa: E501
        :type: int
        """
        self._line_starting_number = line_starting_number

    @property
    def orientation(self):
        """Gets the orientation of this PageSetup.  # noqa: E501

        Gets or sets the orientation of the page. Changing Orientation swaps PageWidth and PageHeight.  # noqa: E501

        :return: The orientation of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PageSetup.

        Gets or sets the orientation of the page. Changing Orientation swaps PageWidth and PageHeight.  # noqa: E501

        :param orientation: The orientation of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["Portrait", "Landscape"]  # noqa: E501
        if not orientation.isdigit():
            if orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation, allowed_values))
            self._orientation = orientation
        else:
            self._orientation = allowed_values[int(orientation) if six.PY3 else long(orientation)]

    @property
    def other_pages_tray(self):
        """Gets the other_pages_tray of this PageSetup.  # noqa: E501

        Gets or sets the paper tray (bin) to be used for all but the first page of a section. The value is implementation (printer) specific.  # noqa: E501

        :return: The other_pages_tray of this PageSetup.  # noqa: E501
        :rtype: int
        """
        return self._other_pages_tray

    @other_pages_tray.setter
    def other_pages_tray(self, other_pages_tray):
        """Sets the other_pages_tray of this PageSetup.

        Gets or sets the paper tray (bin) to be used for all but the first page of a section. The value is implementation (printer) specific.  # noqa: E501

        :param other_pages_tray: The other_pages_tray of this PageSetup.  # noqa: E501
        :type: int
        """
        self._other_pages_tray = other_pages_tray

    @property
    def page_height(self):
        """Gets the page_height of this PageSetup.  # noqa: E501

        Gets or sets the height of the page in points.  # noqa: E501

        :return: The page_height of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._page_height

    @page_height.setter
    def page_height(self, page_height):
        """Sets the page_height of this PageSetup.

        Gets or sets the height of the page in points.  # noqa: E501

        :param page_height: The page_height of this PageSetup.  # noqa: E501
        :type: float
        """
        self._page_height = page_height

    @property
    def page_number_style(self):
        """Gets the page_number_style of this PageSetup.  # noqa: E501

        Gets or sets the page number format.  # noqa: E501

        :return: The page_number_style of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._page_number_style

    @page_number_style.setter
    def page_number_style(self, page_number_style):
        """Sets the page_number_style of this PageSetup.

        Gets or sets the page number format.  # noqa: E501

        :param page_number_style: The page_number_style of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["Arabic", "UppercaseRoman", "LowercaseRoman", "UppercaseLetter", "LowercaseLetter", "Ordinal", "Number", "OrdinalText", "Hex", "ChicagoManual", "Kanji", "KanjiDigit", "AiueoHalfWidth", "IrohaHalfWidth", "ArabicFullWidth", "ArabicHalfWidth", "KanjiTraditional", "KanjiTraditional2", "NumberInCircle", "DecimalFullWidth", "Aiueo", "Iroha", "LeadingZero", "Bullet", "Ganada", "Chosung", "GB1", "GB2", "GB3", "GB4", "Zodiac1", "Zodiac2", "Zodiac3", "TradChinNum1", "TradChinNum2", "TradChinNum3", "TradChinNum4", "SimpChinNum1", "SimpChinNum2", "SimpChinNum3", "SimpChinNum4", "HanjaRead", "HanjaReadDigit", "Hangul", "Hanja", "Hebrew1", "Arabic1", "Hebrew2", "Arabic2", "HindiLetter1", "HindiLetter2", "HindiArabic", "HindiCardinalText", "ThaiLetter", "ThaiArabic", "ThaiCardinalText", "VietCardinalText", "NumberInDash", "LowercaseRussian", "UppercaseRussian", "None", "Custom"]  # noqa: E501
        if not page_number_style.isdigit():
            if page_number_style not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_number_style` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_number_style, allowed_values))
            self._page_number_style = page_number_style
        else:
            self._page_number_style = allowed_values[int(page_number_style) if six.PY3 else long(page_number_style)]

    @property
    def page_starting_number(self):
        """Gets the page_starting_number of this PageSetup.  # noqa: E501

        Gets or sets the starting page number of the section. The RestartPageNumbering property, if set to false, will override the PageStartingNumber property so that page numbering can continue from the previous section.  # noqa: E501

        :return: The page_starting_number of this PageSetup.  # noqa: E501
        :rtype: int
        """
        return self._page_starting_number

    @page_starting_number.setter
    def page_starting_number(self, page_starting_number):
        """Sets the page_starting_number of this PageSetup.

        Gets or sets the starting page number of the section. The RestartPageNumbering property, if set to false, will override the PageStartingNumber property so that page numbering can continue from the previous section.  # noqa: E501

        :param page_starting_number: The page_starting_number of this PageSetup.  # noqa: E501
        :type: int
        """
        self._page_starting_number = page_starting_number

    @property
    def page_width(self):
        """Gets the page_width of this PageSetup.  # noqa: E501

        Gets or sets the width of the page in points.  # noqa: E501

        :return: The page_width of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._page_width

    @page_width.setter
    def page_width(self, page_width):
        """Sets the page_width of this PageSetup.

        Gets or sets the width of the page in points.  # noqa: E501

        :param page_width: The page_width of this PageSetup.  # noqa: E501
        :type: float
        """
        self._page_width = page_width

    @property
    def paper_size(self):
        """Gets the paper_size of this PageSetup.  # noqa: E501

        Gets or sets the paper size. Setting this property updates PageWidth and PageHeight values. Setting this value to Custom does not change existing values.  # noqa: E501

        :return: The paper_size of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._paper_size

    @paper_size.setter
    def paper_size(self, paper_size):
        """Sets the paper_size of this PageSetup.

        Gets or sets the paper size. Setting this property updates PageWidth and PageHeight values. Setting this value to Custom does not change existing values.  # noqa: E501

        :param paper_size: The paper_size of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["A3", "A4", "A5", "B4", "B5", "Executive", "Folio", "Ledger", "Legal", "Letter", "EnvelopeDL", "Quarto", "Statement", "Tabloid", "Paper10x14", "Paper11x17", "Number10Envelope", "JisB4", "JisB5", "Custom"]  # noqa: E501
        if not paper_size.isdigit():
            if paper_size not in allowed_values:
                raise ValueError(
                    "Invalid value for `paper_size` ({0}), must be one of {1}"  # noqa: E501
                    .format(paper_size, allowed_values))
            self._paper_size = paper_size
        else:
            self._paper_size = allowed_values[int(paper_size) if six.PY3 else long(paper_size)]

    @property
    def restart_page_numbering(self):
        """Gets the restart_page_numbering of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether page numbering restarts at the beginning of the section. If set to false, the RestartPageNumbering property will override the PageStartingNumber property so that page numbering can continue from the previous section.  # noqa: E501

        :return: The restart_page_numbering of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._restart_page_numbering

    @restart_page_numbering.setter
    def restart_page_numbering(self, restart_page_numbering):
        """Sets the restart_page_numbering of this PageSetup.

        Gets or sets a value indicating whether page numbering restarts at the beginning of the section. If set to false, the RestartPageNumbering property will override the PageStartingNumber property so that page numbering can continue from the previous section.  # noqa: E501

        :param restart_page_numbering: The restart_page_numbering of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._restart_page_numbering = restart_page_numbering

    @property
    def right_margin(self):
        """Gets the right_margin of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the right edge of the page and the right boundary of the body text.  # noqa: E501

        :return: The right_margin of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """Sets the right_margin of this PageSetup.

        Gets or sets the distance (in points) between the right edge of the page and the right boundary of the body text.  # noqa: E501

        :param right_margin: The right_margin of this PageSetup.  # noqa: E501
        :type: float
        """
        self._right_margin = right_margin

    @property
    def rtl_gutter(self):
        """Gets the rtl_gutter of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether Microsoft Word uses gutters for the section based on a right-to-left language or a left-to-right language.  # noqa: E501

        :return: The rtl_gutter of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._rtl_gutter

    @rtl_gutter.setter
    def rtl_gutter(self, rtl_gutter):
        """Sets the rtl_gutter of this PageSetup.

        Gets or sets a value indicating whether Microsoft Word uses gutters for the section based on a right-to-left language or a left-to-right language.  # noqa: E501

        :param rtl_gutter: The rtl_gutter of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._rtl_gutter = rtl_gutter

    @property
    def section_start(self):
        """Gets the section_start of this PageSetup.  # noqa: E501

        Gets or sets the type of section break for the specified object.  # noqa: E501

        :return: The section_start of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._section_start

    @section_start.setter
    def section_start(self, section_start):
        """Sets the section_start of this PageSetup.

        Gets or sets the type of section break for the specified object.  # noqa: E501

        :param section_start: The section_start of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["Continuous", "NewColumn", "NewPage", "EvenPage", "OddPage"]  # noqa: E501
        if not section_start.isdigit():
            if section_start not in allowed_values:
                raise ValueError(
                    "Invalid value for `section_start` ({0}), must be one of {1}"  # noqa: E501
                    .format(section_start, allowed_values))
            self._section_start = section_start
        else:
            self._section_start = allowed_values[int(section_start) if six.PY3 else long(section_start)]

    @property
    def suppress_endnotes(self):
        """Gets the suppress_endnotes of this PageSetup.  # noqa: E501

        Gets or sets a value indicating whether endnotes are printed at the end of the next section that doesn't suppress endnotes. Suppressed endnotes are printed before the endnotes in that section.  # noqa: E501

        :return: The suppress_endnotes of this PageSetup.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_endnotes

    @suppress_endnotes.setter
    def suppress_endnotes(self, suppress_endnotes):
        """Sets the suppress_endnotes of this PageSetup.

        Gets or sets a value indicating whether endnotes are printed at the end of the next section that doesn't suppress endnotes. Suppressed endnotes are printed before the endnotes in that section.  # noqa: E501

        :param suppress_endnotes: The suppress_endnotes of this PageSetup.  # noqa: E501
        :type: bool
        """
        self._suppress_endnotes = suppress_endnotes

    @property
    def top_margin(self):
        """Gets the top_margin of this PageSetup.  # noqa: E501

        Gets or sets the distance (in points) between the top edge of the page and the top boundary of the body text.  # noqa: E501

        :return: The top_margin of this PageSetup.  # noqa: E501
        :rtype: float
        """
        return self._top_margin

    @top_margin.setter
    def top_margin(self, top_margin):
        """Sets the top_margin of this PageSetup.

        Gets or sets the distance (in points) between the top edge of the page and the top boundary of the body text.  # noqa: E501

        :param top_margin: The top_margin of this PageSetup.  # noqa: E501
        :type: float
        """
        self._top_margin = top_margin

    @property
    def vertical_alignment(self):
        """Gets the vertical_alignment of this PageSetup.  # noqa: E501

        Gets or sets the vertical alignment of text on each page in the document.or section.  # noqa: E501

        :return: The vertical_alignment of this PageSetup.  # noqa: E501
        :rtype: str
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """Sets the vertical_alignment of this PageSetup.

        Gets or sets the vertical alignment of text on each page in the document.or section.  # noqa: E501

        :param vertical_alignment: The vertical_alignment of this PageSetup.  # noqa: E501
        :type: str
        """
        allowed_values = ["Top", "Center", "Justify", "Bottom"]  # noqa: E501
        if not vertical_alignment.isdigit():
            if vertical_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `vertical_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(vertical_alignment, allowed_values))
            self._vertical_alignment = vertical_alignment
        else:
            self._vertical_alignment = allowed_values[int(vertical_alignment) if six.PY3 else long(vertical_alignment)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()































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
        if not isinstance(other, PageSetup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other