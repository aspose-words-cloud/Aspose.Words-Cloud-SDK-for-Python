# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="paragraph_format.py">
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

class ParagraphFormat(object):
    """Paragraph format element.
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
        'add_space_between_far_east_and_alpha': 'bool',
        'add_space_between_far_east_and_digit': 'bool',
        'alignment': 'str',
        'bidi': 'bool',
        'drop_cap_position': 'str',
        'first_line_indent': 'float',
        'keep_together': 'bool',
        'keep_with_next': 'bool',
        'left_indent': 'float',
        'line_spacing': 'float',
        'line_spacing_rule': 'str',
        'lines_to_drop': 'int',
        'no_space_between_paragraphs_of_same_style': 'bool',
        'outline_level': 'str',
        'page_break_before': 'bool',
        'right_indent': 'float',
        'space_after': 'float',
        'space_after_auto': 'bool',
        'space_before': 'float',
        'space_before_auto': 'bool',
        'style_identifier': 'str',
        'style_name': 'str',
        'suppress_auto_hyphens': 'bool',
        'suppress_line_numbers': 'bool',
        'widow_control': 'bool',
        'shading': 'Shading',
        'is_list_item': 'bool',
        'is_heading': 'bool'
    }

    attribute_map = {
        'link': 'Link',
        'add_space_between_far_east_and_alpha': 'AddSpaceBetweenFarEastAndAlpha',
        'add_space_between_far_east_and_digit': 'AddSpaceBetweenFarEastAndDigit',
        'alignment': 'Alignment',
        'bidi': 'Bidi',
        'drop_cap_position': 'DropCapPosition',
        'first_line_indent': 'FirstLineIndent',
        'keep_together': 'KeepTogether',
        'keep_with_next': 'KeepWithNext',
        'left_indent': 'LeftIndent',
        'line_spacing': 'LineSpacing',
        'line_spacing_rule': 'LineSpacingRule',
        'lines_to_drop': 'LinesToDrop',
        'no_space_between_paragraphs_of_same_style': 'NoSpaceBetweenParagraphsOfSameStyle',
        'outline_level': 'OutlineLevel',
        'page_break_before': 'PageBreakBefore',
        'right_indent': 'RightIndent',
        'space_after': 'SpaceAfter',
        'space_after_auto': 'SpaceAfterAuto',
        'space_before': 'SpaceBefore',
        'space_before_auto': 'SpaceBeforeAuto',
        'style_identifier': 'StyleIdentifier',
        'style_name': 'StyleName',
        'suppress_auto_hyphens': 'SuppressAutoHyphens',
        'suppress_line_numbers': 'SuppressLineNumbers',
        'widow_control': 'WidowControl',
        'shading': 'Shading',
        'is_list_item': 'IsListItem',
        'is_heading': 'IsHeading'
    }

    def __init__(self, link=None, add_space_between_far_east_and_alpha=None, add_space_between_far_east_and_digit=None, alignment=None, bidi=None, drop_cap_position=None, first_line_indent=None, keep_together=None, keep_with_next=None, left_indent=None, line_spacing=None, line_spacing_rule=None, lines_to_drop=None, no_space_between_paragraphs_of_same_style=None, outline_level=None, page_break_before=None, right_indent=None, space_after=None, space_after_auto=None, space_before=None, space_before_auto=None, style_identifier=None, style_name=None, suppress_auto_hyphens=None, suppress_line_numbers=None, widow_control=None, shading=None, is_list_item=None, is_heading=None):  # noqa: E501
        """ParagraphFormat - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._add_space_between_far_east_and_alpha = None
        self._add_space_between_far_east_and_digit = None
        self._alignment = None
        self._bidi = None
        self._drop_cap_position = None
        self._first_line_indent = None
        self._keep_together = None
        self._keep_with_next = None
        self._left_indent = None
        self._line_spacing = None
        self._line_spacing_rule = None
        self._lines_to_drop = None
        self._no_space_between_paragraphs_of_same_style = None
        self._outline_level = None
        self._page_break_before = None
        self._right_indent = None
        self._space_after = None
        self._space_after_auto = None
        self._space_before = None
        self._space_before_auto = None
        self._style_identifier = None
        self._style_name = None
        self._suppress_auto_hyphens = None
        self._suppress_line_numbers = None
        self._widow_control = None
        self._shading = None
        self._is_list_item = None
        self._is_heading = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if add_space_between_far_east_and_alpha is not None:
            self.add_space_between_far_east_and_alpha = add_space_between_far_east_and_alpha
        if add_space_between_far_east_and_digit is not None:
            self.add_space_between_far_east_and_digit = add_space_between_far_east_and_digit
        if alignment is not None:
            self.alignment = alignment
        if bidi is not None:
            self.bidi = bidi
        if drop_cap_position is not None:
            self.drop_cap_position = drop_cap_position
        if first_line_indent is not None:
            self.first_line_indent = first_line_indent
        if keep_together is not None:
            self.keep_together = keep_together
        if keep_with_next is not None:
            self.keep_with_next = keep_with_next
        if left_indent is not None:
            self.left_indent = left_indent
        if line_spacing is not None:
            self.line_spacing = line_spacing
        if line_spacing_rule is not None:
            self.line_spacing_rule = line_spacing_rule
        if lines_to_drop is not None:
            self.lines_to_drop = lines_to_drop
        if no_space_between_paragraphs_of_same_style is not None:
            self.no_space_between_paragraphs_of_same_style = no_space_between_paragraphs_of_same_style
        if outline_level is not None:
            self.outline_level = outline_level
        if page_break_before is not None:
            self.page_break_before = page_break_before
        if right_indent is not None:
            self.right_indent = right_indent
        if space_after is not None:
            self.space_after = space_after
        if space_after_auto is not None:
            self.space_after_auto = space_after_auto
        if space_before is not None:
            self.space_before = space_before
        if space_before_auto is not None:
            self.space_before_auto = space_before_auto
        if style_identifier is not None:
            self.style_identifier = style_identifier
        if style_name is not None:
            self.style_name = style_name
        if suppress_auto_hyphens is not None:
            self.suppress_auto_hyphens = suppress_auto_hyphens
        if suppress_line_numbers is not None:
            self.suppress_line_numbers = suppress_line_numbers
        if widow_control is not None:
            self.widow_control = widow_control
        if shading is not None:
            self.shading = shading
        if is_list_item is not None:
            self.is_list_item = is_list_item
        if is_heading is not None:
            self.is_heading = is_heading

    @property
    def link(self):
        """Gets the link of this ParagraphFormat.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this ParagraphFormat.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ParagraphFormat.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this ParagraphFormat.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def add_space_between_far_east_and_alpha(self):
        """Gets the add_space_between_far_east_and_alpha of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether inter-character spacing is automatically adjusted between regions of Latin text and regions of East Asian text in the current paragraph.  # noqa: E501

        :return: The add_space_between_far_east_and_alpha of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._add_space_between_far_east_and_alpha

    @add_space_between_far_east_and_alpha.setter
    def add_space_between_far_east_and_alpha(self, add_space_between_far_east_and_alpha):
        """Sets the add_space_between_far_east_and_alpha of this ParagraphFormat.

        Gets or sets a value indicating whether inter-character spacing is automatically adjusted between regions of Latin text and regions of East Asian text in the current paragraph.  # noqa: E501

        :param add_space_between_far_east_and_alpha: The add_space_between_far_east_and_alpha of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._add_space_between_far_east_and_alpha = add_space_between_far_east_and_alpha

    @property
    def add_space_between_far_east_and_digit(self):
        """Gets the add_space_between_far_east_and_digit of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether inter-character spacing is automatically adjusted between regions of numbers and regions of East Asian text in the current paragraph.  # noqa: E501

        :return: The add_space_between_far_east_and_digit of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._add_space_between_far_east_and_digit

    @add_space_between_far_east_and_digit.setter
    def add_space_between_far_east_and_digit(self, add_space_between_far_east_and_digit):
        """Sets the add_space_between_far_east_and_digit of this ParagraphFormat.

        Gets or sets a value indicating whether inter-character spacing is automatically adjusted between regions of numbers and regions of East Asian text in the current paragraph.  # noqa: E501

        :param add_space_between_far_east_and_digit: The add_space_between_far_east_and_digit of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._add_space_between_far_east_and_digit = add_space_between_far_east_and_digit

    @property
    def alignment(self):
        """Gets the alignment of this ParagraphFormat.  # noqa: E501

        Gets or sets text alignment for the paragraph.  # noqa: E501

        :return: The alignment of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this ParagraphFormat.

        Gets or sets text alignment for the paragraph.  # noqa: E501

        :param alignment: The alignment of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["Left", "Center", "Right", "Justify", "Distributed", "ArabicMediumKashida", "ArabicHighKashida", "ArabicLowKashida", "ThaiDistributed", "MathElementCenterAsGroup"]  # noqa: E501
        if not alignment.isdigit():
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values))
            self._alignment = alignment
        else:
            self._alignment = allowed_values[int(alignment) if six.PY3 else long(alignment)]

    @property
    def bidi(self):
        """Gets the bidi of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether this is a right-to-left paragraph. When true, the runs and other inline objects in this paragraph are laid out right to left.  # noqa: E501

        :return: The bidi of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._bidi

    @bidi.setter
    def bidi(self, bidi):
        """Sets the bidi of this ParagraphFormat.

        Gets or sets a value indicating whether this is a right-to-left paragraph. When true, the runs and other inline objects in this paragraph are laid out right to left.  # noqa: E501

        :param bidi: The bidi of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._bidi = bidi

    @property
    def drop_cap_position(self):
        """Gets the drop_cap_position of this ParagraphFormat.  # noqa: E501

        Gets or sets the position for a drop cap text.  # noqa: E501

        :return: The drop_cap_position of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._drop_cap_position

    @drop_cap_position.setter
    def drop_cap_position(self, drop_cap_position):
        """Sets the drop_cap_position of this ParagraphFormat.

        Gets or sets the position for a drop cap text.  # noqa: E501

        :param drop_cap_position: The drop_cap_position of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Normal", "Margin"]  # noqa: E501
        if not drop_cap_position.isdigit():
            if drop_cap_position not in allowed_values:
                raise ValueError(
                    "Invalid value for `drop_cap_position` ({0}), must be one of {1}"  # noqa: E501
                    .format(drop_cap_position, allowed_values))
            self._drop_cap_position = drop_cap_position
        else:
            self._drop_cap_position = allowed_values[int(drop_cap_position) if six.PY3 else long(drop_cap_position)]

    @property
    def first_line_indent(self):
        """Gets the first_line_indent of this ParagraphFormat.  # noqa: E501

        Gets or sets the value (in points) for a first line or hanging indent. Use a positive value to set a first-line indent, and use a negative value to set a hanging indent.  # noqa: E501

        :return: The first_line_indent of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._first_line_indent

    @first_line_indent.setter
    def first_line_indent(self, first_line_indent):
        """Sets the first_line_indent of this ParagraphFormat.

        Gets or sets the value (in points) for a first line or hanging indent. Use a positive value to set a first-line indent, and use a negative value to set a hanging indent.  # noqa: E501

        :param first_line_indent: The first_line_indent of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._first_line_indent = first_line_indent

    @property
    def keep_together(self):
        """Gets the keep_together of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether all lines in the paragraph are to remain on the same page.  # noqa: E501

        :return: The keep_together of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._keep_together

    @keep_together.setter
    def keep_together(self, keep_together):
        """Sets the keep_together of this ParagraphFormat.

        Gets or sets a value indicating whether all lines in the paragraph are to remain on the same page.  # noqa: E501

        :param keep_together: The keep_together of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._keep_together = keep_together

    @property
    def keep_with_next(self):
        """Gets the keep_with_next of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the paragraph is to remains on the same page as the paragraph that follows it.  # noqa: E501

        :return: The keep_with_next of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._keep_with_next

    @keep_with_next.setter
    def keep_with_next(self, keep_with_next):
        """Sets the keep_with_next of this ParagraphFormat.

        Gets or sets a value indicating whether the paragraph is to remains on the same page as the paragraph that follows it.  # noqa: E501

        :param keep_with_next: The keep_with_next of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._keep_with_next = keep_with_next

    @property
    def left_indent(self):
        """Gets the left_indent of this ParagraphFormat.  # noqa: E501

        Gets or sets the value (in points), that represents the left indent for paragraph.  # noqa: E501

        :return: The left_indent of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._left_indent

    @left_indent.setter
    def left_indent(self, left_indent):
        """Sets the left_indent of this ParagraphFormat.

        Gets or sets the value (in points), that represents the left indent for paragraph.  # noqa: E501

        :param left_indent: The left_indent of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._left_indent = left_indent

    @property
    def line_spacing(self):
        """Gets the line_spacing of this ParagraphFormat.  # noqa: E501

        Gets or sets the line spacing (in points) for the paragraph. When LineSpacingRule property is set to AtLeast, the line spacing can be greater than or equal to, but never less than the specified LineSpacing value.When LineSpacingRule property is set to Exactly, the line spacing never changes from the specified LineSpacing value, even if a larger font is used within the paragraph.  # noqa: E501

        :return: The line_spacing of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._line_spacing

    @line_spacing.setter
    def line_spacing(self, line_spacing):
        """Sets the line_spacing of this ParagraphFormat.

        Gets or sets the line spacing (in points) for the paragraph. When LineSpacingRule property is set to AtLeast, the line spacing can be greater than or equal to, but never less than the specified LineSpacing value.When LineSpacingRule property is set to Exactly, the line spacing never changes from the specified LineSpacing value, even if a larger font is used within the paragraph.  # noqa: E501

        :param line_spacing: The line_spacing of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._line_spacing = line_spacing

    @property
    def line_spacing_rule(self):
        """Gets the line_spacing_rule of this ParagraphFormat.  # noqa: E501

        Gets or sets the line spacing for the paragraph.  # noqa: E501

        :return: The line_spacing_rule of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._line_spacing_rule

    @line_spacing_rule.setter
    def line_spacing_rule(self, line_spacing_rule):
        """Sets the line_spacing_rule of this ParagraphFormat.

        Gets or sets the line spacing for the paragraph.  # noqa: E501

        :param line_spacing_rule: The line_spacing_rule of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["AtLeast", "Exactly", "Multiple"]  # noqa: E501
        if not line_spacing_rule.isdigit():
            if line_spacing_rule not in allowed_values:
                raise ValueError(
                    "Invalid value for `line_spacing_rule` ({0}), must be one of {1}"  # noqa: E501
                    .format(line_spacing_rule, allowed_values))
            self._line_spacing_rule = line_spacing_rule
        else:
            self._line_spacing_rule = allowed_values[int(line_spacing_rule) if six.PY3 else long(line_spacing_rule)]

    @property
    def lines_to_drop(self):
        """Gets the lines_to_drop of this ParagraphFormat.  # noqa: E501

        Gets or sets the number of lines of the paragraph text used to calculate the drop cap height.  # noqa: E501

        :return: The lines_to_drop of this ParagraphFormat.  # noqa: E501
        :rtype: int
        """
        return self._lines_to_drop

    @lines_to_drop.setter
    def lines_to_drop(self, lines_to_drop):
        """Sets the lines_to_drop of this ParagraphFormat.

        Gets or sets the number of lines of the paragraph text used to calculate the drop cap height.  # noqa: E501

        :param lines_to_drop: The lines_to_drop of this ParagraphFormat.  # noqa: E501
        :type: int
        """
        self._lines_to_drop = lines_to_drop

    @property
    def no_space_between_paragraphs_of_same_style(self):
        """Gets the no_space_between_paragraphs_of_same_style of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether SpaceBefore and SpaceAfter will be ignored between the paragraphs of the same style. This setting only takes affect when applied to a paragraph style. If applied to a paragraph directly, it has no effect.  # noqa: E501

        :return: The no_space_between_paragraphs_of_same_style of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._no_space_between_paragraphs_of_same_style

    @no_space_between_paragraphs_of_same_style.setter
    def no_space_between_paragraphs_of_same_style(self, no_space_between_paragraphs_of_same_style):
        """Sets the no_space_between_paragraphs_of_same_style of this ParagraphFormat.

        Gets or sets a value indicating whether SpaceBefore and SpaceAfter will be ignored between the paragraphs of the same style. This setting only takes affect when applied to a paragraph style. If applied to a paragraph directly, it has no effect.  # noqa: E501

        :param no_space_between_paragraphs_of_same_style: The no_space_between_paragraphs_of_same_style of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._no_space_between_paragraphs_of_same_style = no_space_between_paragraphs_of_same_style

    @property
    def outline_level(self):
        """Gets the outline_level of this ParagraphFormat.  # noqa: E501

        Gets or sets the outline level of the paragraph in the document.  # noqa: E501

        :return: The outline_level of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._outline_level

    @outline_level.setter
    def outline_level(self, outline_level):
        """Sets the outline_level of this ParagraphFormat.

        Gets or sets the outline level of the paragraph in the document.  # noqa: E501

        :param outline_level: The outline_level of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["Level1", "Level2", "Level3", "Level4", "Level5", "Level6", "Level7", "Level8", "Level9", "BodyText"]  # noqa: E501
        if not outline_level.isdigit():
            if outline_level not in allowed_values:
                raise ValueError(
                    "Invalid value for `outline_level` ({0}), must be one of {1}"  # noqa: E501
                    .format(outline_level, allowed_values))
            self._outline_level = outline_level
        else:
            self._outline_level = allowed_values[int(outline_level) if six.PY3 else long(outline_level)]

    @property
    def page_break_before(self):
        """Gets the page_break_before of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether a page break is forced before the paragraph.  # noqa: E501

        :return: The page_break_before of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._page_break_before

    @page_break_before.setter
    def page_break_before(self, page_break_before):
        """Sets the page_break_before of this ParagraphFormat.

        Gets or sets a value indicating whether a page break is forced before the paragraph.  # noqa: E501

        :param page_break_before: The page_break_before of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._page_break_before = page_break_before

    @property
    def right_indent(self):
        """Gets the right_indent of this ParagraphFormat.  # noqa: E501

        Gets or sets the value (in points) that represents the right indent for paragraph.  # noqa: E501

        :return: The right_indent of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._right_indent

    @right_indent.setter
    def right_indent(self, right_indent):
        """Sets the right_indent of this ParagraphFormat.

        Gets or sets the value (in points) that represents the right indent for paragraph.  # noqa: E501

        :param right_indent: The right_indent of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._right_indent = right_indent

    @property
    def space_after(self):
        """Gets the space_after of this ParagraphFormat.  # noqa: E501

        Gets or sets the amount of spacing (in points) after the paragraph. Has no effect when SpaceAfterAuto is true.  # noqa: E501

        :return: The space_after of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._space_after

    @space_after.setter
    def space_after(self, space_after):
        """Sets the space_after of this ParagraphFormat.

        Gets or sets the amount of spacing (in points) after the paragraph. Has no effect when SpaceAfterAuto is true.  # noqa: E501

        :param space_after: The space_after of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._space_after = space_after

    @property
    def space_after_auto(self):
        """Gets the space_after_auto of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the amount of spacing after the paragraph is set automatically. When set to true, overrides the effect of SpaceAfter.  # noqa: E501

        :return: The space_after_auto of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._space_after_auto

    @space_after_auto.setter
    def space_after_auto(self, space_after_auto):
        """Sets the space_after_auto of this ParagraphFormat.

        Gets or sets a value indicating whether the amount of spacing after the paragraph is set automatically. When set to true, overrides the effect of SpaceAfter.  # noqa: E501

        :param space_after_auto: The space_after_auto of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._space_after_auto = space_after_auto

    @property
    def space_before(self):
        """Gets the space_before of this ParagraphFormat.  # noqa: E501

        Gets or sets the amount of spacing (in points) before the paragraph. Has no effect when SpaceBeforeAuto is true.  # noqa: E501

        :return: The space_before of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._space_before

    @space_before.setter
    def space_before(self, space_before):
        """Sets the space_before of this ParagraphFormat.

        Gets or sets the amount of spacing (in points) before the paragraph. Has no effect when SpaceBeforeAuto is true.  # noqa: E501

        :param space_before: The space_before of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._space_before = space_before

    @property
    def space_before_auto(self):
        """Gets the space_before_auto of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the amount of spacing before the paragraph is set automatically. When set to true, overrides the effect of SpaceBefore.  # noqa: E501

        :return: The space_before_auto of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._space_before_auto

    @space_before_auto.setter
    def space_before_auto(self, space_before_auto):
        """Sets the space_before_auto of this ParagraphFormat.

        Gets or sets a value indicating whether the amount of spacing before the paragraph is set automatically. When set to true, overrides the effect of SpaceBefore.  # noqa: E501

        :param space_before_auto: The space_before_auto of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._space_before_auto = space_before_auto

    @property
    def style_identifier(self):
        """Gets the style_identifier of this ParagraphFormat.  # noqa: E501

        Gets or sets the locale independent style identifier of the paragraph style applied to this formatting.  # noqa: E501

        :return: The style_identifier of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._style_identifier

    @style_identifier.setter
    def style_identifier(self, style_identifier):
        """Sets the style_identifier of this ParagraphFormat.

        Gets or sets the locale independent style identifier of the paragraph style applied to this formatting.  # noqa: E501

        :param style_identifier: The style_identifier of this ParagraphFormat.  # noqa: E501
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
        """Gets the style_name of this ParagraphFormat.  # noqa: E501

        Gets or sets the name of the paragraph style applied to this formatting.  # noqa: E501

        :return: The style_name of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._style_name

    @style_name.setter
    def style_name(self, style_name):
        """Sets the style_name of this ParagraphFormat.

        Gets or sets the name of the paragraph style applied to this formatting.  # noqa: E501

        :param style_name: The style_name of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        self._style_name = style_name

    @property
    def suppress_auto_hyphens(self):
        """Gets the suppress_auto_hyphens of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the current paragraph should be exempted from any hyphenation which is applied in the document settings.  # noqa: E501

        :return: The suppress_auto_hyphens of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_auto_hyphens

    @suppress_auto_hyphens.setter
    def suppress_auto_hyphens(self, suppress_auto_hyphens):
        """Sets the suppress_auto_hyphens of this ParagraphFormat.

        Gets or sets a value indicating whether the current paragraph should be exempted from any hyphenation which is applied in the document settings.  # noqa: E501

        :param suppress_auto_hyphens: The suppress_auto_hyphens of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._suppress_auto_hyphens = suppress_auto_hyphens

    @property
    def suppress_line_numbers(self):
        """Gets the suppress_line_numbers of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the current paragraph's lines should be exempted from line numbering which is applied in the parent section.  # noqa: E501

        :return: The suppress_line_numbers of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_line_numbers

    @suppress_line_numbers.setter
    def suppress_line_numbers(self, suppress_line_numbers):
        """Sets the suppress_line_numbers of this ParagraphFormat.

        Gets or sets a value indicating whether the current paragraph's lines should be exempted from line numbering which is applied in the parent section.  # noqa: E501

        :param suppress_line_numbers: The suppress_line_numbers of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._suppress_line_numbers = suppress_line_numbers

    @property
    def widow_control(self):
        """Gets the widow_control of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the first and last lines in the paragraph are to remain on the same page as the rest of the paragraph.  # noqa: E501

        :return: The widow_control of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._widow_control

    @widow_control.setter
    def widow_control(self, widow_control):
        """Sets the widow_control of this ParagraphFormat.

        Gets or sets a value indicating whether the first and last lines in the paragraph are to remain on the same page as the rest of the paragraph.  # noqa: E501

        :param widow_control: The widow_control of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._widow_control = widow_control

    @property
    def shading(self):
        """Gets the shading of this ParagraphFormat.  # noqa: E501

        Gets or sets the Shading object, that refers to the shading formatting for the paragraph.  # noqa: E501

        :return: The shading of this ParagraphFormat.  # noqa: E501
        :rtype: Shading
        """
        return self._shading

    @shading.setter
    def shading(self, shading):
        """Sets the shading of this ParagraphFormat.

        Gets or sets the Shading object, that refers to the shading formatting for the paragraph.  # noqa: E501

        :param shading: The shading of this ParagraphFormat.  # noqa: E501
        :type: Shading
        """
        self._shading = shading

    @property
    def is_list_item(self):
        """Gets the is_list_item of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the paragraph is an item in a bulleted or numbered list.  # noqa: E501

        :return: The is_list_item of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._is_list_item

    @is_list_item.setter
    def is_list_item(self, is_list_item):
        """Sets the is_list_item of this ParagraphFormat.

        Gets or sets a value indicating whether the paragraph is an item in a bulleted or numbered list.  # noqa: E501

        :param is_list_item: The is_list_item of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._is_list_item = is_list_item

    @property
    def is_heading(self):
        """Gets the is_heading of this ParagraphFormat.  # noqa: E501

        Gets or sets a value indicating whether the paragraph style is one of the built-in Heading styles.  # noqa: E501

        :return: The is_heading of this ParagraphFormat.  # noqa: E501
        :rtype: bool
        """
        return self._is_heading

    @is_heading.setter
    def is_heading(self, is_heading):
        """Sets the is_heading of this ParagraphFormat.

        Gets or sets a value indicating whether the paragraph style is one of the built-in Heading styles.  # noqa: E501

        :param is_heading: The is_heading of this ParagraphFormat.  # noqa: E501
        :type: bool
        """
        self._is_heading = is_heading


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()




























        if self._shading is not None:
            self._shading.validate()




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
        if not isinstance(other, ParagraphFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other