# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="text_save_options_data.py">
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

class TextSaveOptionsData(object):
    """Container class for text save options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_embedding_post_script_fonts': 'bool',
        'custom_time_zone_info_data': 'TimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'str',
        'dml_effects_rendering_mode': 'str',
        'dml_rendering_mode': 'str',
        'file_name': 'str',
        'iml_rendering_mode': 'str',
        'update_ambiguous_text_font': 'bool',
        'update_created_time_property': 'bool',
        'update_fields': 'bool',
        'update_last_printed_property': 'bool',
        'update_last_saved_time_property': 'bool',
        'zip_output': 'bool',
        'encoding': 'str',
        'export_headers_footers_mode': 'str',
        'force_page_breaks': 'bool',
        'paragraph_break': 'str',
        'add_bidi_marks': 'bool',
        'max_characters_per_line': 'int',
        'office_math_export_mode': 'str',
        'preserve_table_layout': 'bool',
        'simplify_list_labels': 'bool',
        'save_format': 'str'
    }

    attribute_map = {
        'allow_embedding_post_script_fonts': 'AllowEmbeddingPostScriptFonts',
        'custom_time_zone_info_data': 'CustomTimeZoneInfoData',
        'dml3_d_effects_rendering_mode': 'Dml3DEffectsRenderingMode',
        'dml_effects_rendering_mode': 'DmlEffectsRenderingMode',
        'dml_rendering_mode': 'DmlRenderingMode',
        'file_name': 'FileName',
        'iml_rendering_mode': 'ImlRenderingMode',
        'update_ambiguous_text_font': 'UpdateAmbiguousTextFont',
        'update_created_time_property': 'UpdateCreatedTimeProperty',
        'update_fields': 'UpdateFields',
        'update_last_printed_property': 'UpdateLastPrintedProperty',
        'update_last_saved_time_property': 'UpdateLastSavedTimeProperty',
        'zip_output': 'ZipOutput',
        'encoding': 'Encoding',
        'export_headers_footers_mode': 'ExportHeadersFootersMode',
        'force_page_breaks': 'ForcePageBreaks',
        'paragraph_break': 'ParagraphBreak',
        'add_bidi_marks': 'AddBidiMarks',
        'max_characters_per_line': 'MaxCharactersPerLine',
        'office_math_export_mode': 'OfficeMathExportMode',
        'preserve_table_layout': 'PreserveTableLayout',
        'simplify_list_labels': 'SimplifyListLabels',
        'save_format': 'SaveFormat'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, iml_rendering_mode=None, update_ambiguous_text_font=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, zip_output=None, encoding=None, export_headers_footers_mode=None, force_page_breaks=None, paragraph_break=None, add_bidi_marks=None, max_characters_per_line=None, office_math_export_mode=None, preserve_table_layout=None, simplify_list_labels=None):  # noqa: E501
        """TextSaveOptionsData - a model defined in Swagger"""  # noqa: E501

        self._allow_embedding_post_script_fonts = None
        self._custom_time_zone_info_data = None
        self._dml3_d_effects_rendering_mode = None
        self._dml_effects_rendering_mode = None
        self._dml_rendering_mode = None
        self._file_name = None
        self._iml_rendering_mode = None
        self._update_ambiguous_text_font = None
        self._update_created_time_property = None
        self._update_fields = None
        self._update_last_printed_property = None
        self._update_last_saved_time_property = None
        self._zip_output = None
        self._encoding = None
        self._export_headers_footers_mode = None
        self._force_page_breaks = None
        self._paragraph_break = None
        self._add_bidi_marks = None
        self._max_characters_per_line = None
        self._office_math_export_mode = None
        self._preserve_table_layout = None
        self._simplify_list_labels = None
        self._save_format = "txt"
        self.discriminator = None

        if allow_embedding_post_script_fonts is not None:
            self.allow_embedding_post_script_fonts = allow_embedding_post_script_fonts
        if custom_time_zone_info_data is not None:
            self.custom_time_zone_info_data = custom_time_zone_info_data
        if dml3_d_effects_rendering_mode is not None:
            self.dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        if dml_effects_rendering_mode is not None:
            self.dml_effects_rendering_mode = dml_effects_rendering_mode
        if dml_rendering_mode is not None:
            self.dml_rendering_mode = dml_rendering_mode
        if file_name is not None:
            self.file_name = file_name
        if iml_rendering_mode is not None:
            self.iml_rendering_mode = iml_rendering_mode
        if update_ambiguous_text_font is not None:
            self.update_ambiguous_text_font = update_ambiguous_text_font
        if update_created_time_property is not None:
            self.update_created_time_property = update_created_time_property
        if update_fields is not None:
            self.update_fields = update_fields
        if update_last_printed_property is not None:
            self.update_last_printed_property = update_last_printed_property
        if update_last_saved_time_property is not None:
            self.update_last_saved_time_property = update_last_saved_time_property
        if zip_output is not None:
            self.zip_output = zip_output
        if encoding is not None:
            self.encoding = encoding
        if export_headers_footers_mode is not None:
            self.export_headers_footers_mode = export_headers_footers_mode
        if force_page_breaks is not None:
            self.force_page_breaks = force_page_breaks
        if paragraph_break is not None:
            self.paragraph_break = paragraph_break
        if add_bidi_marks is not None:
            self.add_bidi_marks = add_bidi_marks
        if max_characters_per_line is not None:
            self.max_characters_per_line = max_characters_per_line
        if office_math_export_mode is not None:
            self.office_math_export_mode = office_math_export_mode
        if preserve_table_layout is not None:
            self.preserve_table_layout = preserve_table_layout
        if simplify_list_labels is not None:
            self.simplify_list_labels = simplify_list_labels

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this TextSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this TextSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this TextSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this TextSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this TextSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this TextSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Basic", "Advanced"]  # noqa: E501
        if not dml3_d_effects_rendering_mode.isdigit():
            if dml3_d_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml3_d_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml3_d_effects_rendering_mode, allowed_values))
            self._dml3_d_effects_rendering_mode = dml3_d_effects_rendering_mode
        else:
            self._dml3_d_effects_rendering_mode = allowed_values[int(dml3_d_effects_rendering_mode) if six.PY3 else long(dml3_d_effects_rendering_mode)]

    @property
    def dml_effects_rendering_mode(self):
        """Gets the dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this TextSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Simplified", "None", "Fine"]  # noqa: E501
        if not dml_effects_rendering_mode.isdigit():
            if dml_effects_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml_effects_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml_effects_rendering_mode, allowed_values))
            self._dml_effects_rendering_mode = dml_effects_rendering_mode
        else:
            self._dml_effects_rendering_mode = allowed_values[int(dml_effects_rendering_mode) if six.PY3 else long(dml_effects_rendering_mode)]

    @property
    def dml_rendering_mode(self):
        """Gets the dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this TextSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Fallback", "DrawingML"]  # noqa: E501
        if not dml_rendering_mode.isdigit():
            if dml_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `dml_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(dml_rendering_mode, allowed_values))
            self._dml_rendering_mode = dml_rendering_mode
        else:
            self._dml_rendering_mode = allowed_values[int(dml_rendering_mode) if six.PY3 else long(dml_rendering_mode)]

    @property
    def file_name(self):
        """Gets the file_name of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TextSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :return: The iml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this TextSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Fallback", "InkML"]  # noqa: E501
        if not iml_rendering_mode.isdigit():
            if iml_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `iml_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(iml_rendering_mode, allowed_values))
            self._iml_rendering_mode = iml_rendering_mode
        else:
            self._iml_rendering_mode = allowed_values[int(iml_rendering_mode) if six.PY3 else long(iml_rendering_mode)]

    @property
    def update_ambiguous_text_font(self):
        """Gets the update_ambiguous_text_font of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :return: The update_ambiguous_text_font of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_ambiguous_text_font

    @update_ambiguous_text_font.setter
    def update_ambiguous_text_font(self, update_ambiguous_text_font):
        """Sets the update_ambiguous_text_font of this TextSaveOptionsData.

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :param update_ambiguous_text_font: The update_ambiguous_text_font of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_ambiguous_text_font = update_ambiguous_text_font

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_created_time_property of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this TextSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this TextSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this TextSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this TextSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def zip_output(self):
        """Gets the zip_output of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :return: The zip_output of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this TextSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :param zip_output: The zip_output of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def encoding(self):
        """Gets the encoding of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the character encoding to use when exporting in plain text format.  # noqa: E501

        :return: The encoding of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this TextSaveOptionsData.

        Gets or sets the character encoding to use when exporting in plain text format.  # noqa: E501

        :param encoding: The encoding of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding

    @property
    def export_headers_footers_mode(self):
        """Gets the export_headers_footers_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls whether to output headers and footers when exporting in plain text format. The default value is TxtExportHeadersFootersMode.PrimaryOnly.  # noqa: E501

        :return: The export_headers_footers_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_headers_footers_mode

    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, export_headers_footers_mode):
        """Sets the export_headers_footers_mode of this TextSaveOptionsData.

        Gets or sets the option that controls whether to output headers and footers when exporting in plain text format. The default value is TxtExportHeadersFootersMode.PrimaryOnly.  # noqa: E501

        :param export_headers_footers_mode: The export_headers_footers_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "PrimaryOnly", "AllAtEnd"]  # noqa: E501
        if not export_headers_footers_mode.isdigit():
            if export_headers_footers_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `export_headers_footers_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(export_headers_footers_mode, allowed_values))
            self._export_headers_footers_mode = export_headers_footers_mode
        else:
            self._export_headers_footers_mode = allowed_values[int(export_headers_footers_mode) if six.PY3 else long(export_headers_footers_mode)]

    @property
    def force_page_breaks(self):
        """Gets the force_page_breaks of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :return: The force_page_breaks of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._force_page_breaks

    @force_page_breaks.setter
    def force_page_breaks(self, force_page_breaks):
        """Sets the force_page_breaks of this TextSaveOptionsData.

        Gets or sets a value indicating whether the page breaks should be preserved during export. The default value is false.  # noqa: E501

        :param force_page_breaks: The force_page_breaks of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._force_page_breaks = force_page_breaks

    @property
    def paragraph_break(self):
        """Gets the paragraph_break of this TextSaveOptionsData.  # noqa: E501

        Gets or sets the string to use as a paragraph break when exporting in plain text format.  # noqa: E501

        :return: The paragraph_break of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._paragraph_break

    @paragraph_break.setter
    def paragraph_break(self, paragraph_break):
        """Sets the paragraph_break of this TextSaveOptionsData.

        Gets or sets the string to use as a paragraph break when exporting in plain text format.  # noqa: E501

        :param paragraph_break: The paragraph_break of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._paragraph_break = paragraph_break

    @property
    def add_bidi_marks(self):
        """Gets the add_bidi_marks of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to add bi-directional marks before each BiDi run when exporting in plain text format. The default value is true.  # noqa: E501

        :return: The add_bidi_marks of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._add_bidi_marks

    @add_bidi_marks.setter
    def add_bidi_marks(self, add_bidi_marks):
        """Sets the add_bidi_marks of this TextSaveOptionsData.

        Gets or sets a value indicating whether to add bi-directional marks before each BiDi run when exporting in plain text format. The default value is true.  # noqa: E501

        :param add_bidi_marks: The add_bidi_marks of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._add_bidi_marks = add_bidi_marks

    @property
    def max_characters_per_line(self):
        """Gets the max_characters_per_line of this TextSaveOptionsData.  # noqa: E501

        Gets or sets an integer value that specifies the maximum number of characters per one line. The default value is 0, that means no limit.  # noqa: E501

        :return: The max_characters_per_line of this TextSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._max_characters_per_line

    @max_characters_per_line.setter
    def max_characters_per_line(self, max_characters_per_line):
        """Sets the max_characters_per_line of this TextSaveOptionsData.

        Gets or sets an integer value that specifies the maximum number of characters per one line. The default value is 0, that means no limit.  # noqa: E501

        :param max_characters_per_line: The max_characters_per_line of this TextSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._max_characters_per_line = max_characters_per_line

    @property
    def office_math_export_mode(self):
        """Gets the office_math_export_mode of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value that specifies how OfficeMath will be written to the output file. The default value is Text.  # noqa: E501

        :return: The office_math_export_mode of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._office_math_export_mode

    @office_math_export_mode.setter
    def office_math_export_mode(self, office_math_export_mode):
        """Sets the office_math_export_mode of this TextSaveOptionsData.

        Gets or sets a value that specifies how OfficeMath will be written to the output file. The default value is Text.  # noqa: E501

        :param office_math_export_mode: The office_math_export_mode of this TextSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Text", "Latex"]  # noqa: E501
        if not office_math_export_mode.isdigit():
            if office_math_export_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `office_math_export_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(office_math_export_mode, allowed_values))
            self._office_math_export_mode = office_math_export_mode
        else:
            self._office_math_export_mode = allowed_values[int(office_math_export_mode) if six.PY3 else long(office_math_export_mode)]

    @property
    def preserve_table_layout(self):
        """Gets the preserve_table_layout of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the program should attempt to preserve layout of tables when saving in the plain text format.  # noqa: E501

        :return: The preserve_table_layout of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._preserve_table_layout

    @preserve_table_layout.setter
    def preserve_table_layout(self, preserve_table_layout):
        """Sets the preserve_table_layout of this TextSaveOptionsData.

        Gets or sets a value indicating whether the program should attempt to preserve layout of tables when saving in the plain text format.  # noqa: E501

        :param preserve_table_layout: The preserve_table_layout of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._preserve_table_layout = preserve_table_layout

    @property
    def simplify_list_labels(self):
        """Gets the simplify_list_labels of this TextSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the program should simplify list labels in case of complex label formatting not being adequately represented by plain text.  # noqa: E501

        :return: The simplify_list_labels of this TextSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._simplify_list_labels

    @simplify_list_labels.setter
    def simplify_list_labels(self, simplify_list_labels):
        """Sets the simplify_list_labels of this TextSaveOptionsData.

        Gets or sets a value indicating whether the program should simplify list labels in case of complex label formatting not being adequately represented by plain text.  # noqa: E501

        :param simplify_list_labels: The simplify_list_labels of this TextSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._simplify_list_labels = simplify_list_labels

    @property
    def save_format(self):
        """Gets the save_format of this TextSaveOptionsData.  # noqa: E501

        Gets the format of save.  # noqa: E501

        :return: The save_format of this TextSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format



    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._file_name is None:
            raise ValueError("Property FileName in TextSaveOptionsData is required.")  # noqa: E501
        if self._max_characters_per_line is None:
            raise ValueError("Property MaxCharactersPerLine in TextSaveOptionsData is required.")  # noqa: E501

        if self._custom_time_zone_info_data is not None:
            self._custom_time_zone_info_data.validate()























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
        if not isinstance(other, TextSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other