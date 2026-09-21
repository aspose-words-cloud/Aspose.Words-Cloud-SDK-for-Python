# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="html_fixed_save_options_data.py">
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

class HtmlFixedSaveOptionsData(object):
    """Container class for fixed html save options.
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
        'color_mode': 'str',
        'jpeg_quality': 'int',
        'metafile_rendering_options': 'MetafileRenderingOptionsData',
        'numeral_format': 'str',
        'optimize_output': 'bool',
        'page_count': 'int',
        'page_index': 'int',
        'css_class_names_prefix': 'str',
        'encoding': 'str',
        'export_embedded_css': 'bool',
        'export_embedded_fonts': 'bool',
        'export_embedded_images': 'bool',
        'export_form_fields': 'bool',
        'font_format': 'str',
        'id_prefix': 'str',
        'page_horizontal_alignment': 'str',
        'page_margins': 'float',
        'resources_folder': 'str',
        'resources_folder_alias': 'str',
        'save_font_face_css_separately': 'bool',
        'show_page_border': 'bool',
        'use_target_machine_fonts': 'bool',
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
        'color_mode': 'ColorMode',
        'jpeg_quality': 'JpegQuality',
        'metafile_rendering_options': 'MetafileRenderingOptions',
        'numeral_format': 'NumeralFormat',
        'optimize_output': 'OptimizeOutput',
        'page_count': 'PageCount',
        'page_index': 'PageIndex',
        'css_class_names_prefix': 'CssClassNamesPrefix',
        'encoding': 'Encoding',
        'export_embedded_css': 'ExportEmbeddedCss',
        'export_embedded_fonts': 'ExportEmbeddedFonts',
        'export_embedded_images': 'ExportEmbeddedImages',
        'export_form_fields': 'ExportFormFields',
        'font_format': 'FontFormat',
        'id_prefix': 'IdPrefix',
        'page_horizontal_alignment': 'PageHorizontalAlignment',
        'page_margins': 'PageMargins',
        'resources_folder': 'ResourcesFolder',
        'resources_folder_alias': 'ResourcesFolderAlias',
        'save_font_face_css_separately': 'SaveFontFaceCssSeparately',
        'show_page_border': 'ShowPageBorder',
        'use_target_machine_fonts': 'UseTargetMachineFonts',
        'save_format': 'SaveFormat'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, iml_rendering_mode=None, update_ambiguous_text_font=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, zip_output=None, color_mode=None, jpeg_quality=None, metafile_rendering_options=None, numeral_format=None, optimize_output=None, page_count=None, page_index=None, css_class_names_prefix=None, encoding=None, export_embedded_css=None, export_embedded_fonts=None, export_embedded_images=None, export_form_fields=None, font_format=None, id_prefix=None, page_horizontal_alignment=None, page_margins=None, resources_folder=None, resources_folder_alias=None, save_font_face_css_separately=None, show_page_border=None, use_target_machine_fonts=None):  # noqa: E501
        """HtmlFixedSaveOptionsData - a model defined in Swagger"""  # noqa: E501

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
        self._color_mode = None
        self._jpeg_quality = None
        self._metafile_rendering_options = None
        self._numeral_format = None
        self._optimize_output = None
        self._page_count = None
        self._page_index = None
        self._css_class_names_prefix = None
        self._encoding = None
        self._export_embedded_css = None
        self._export_embedded_fonts = None
        self._export_embedded_images = None
        self._export_form_fields = None
        self._font_format = None
        self._id_prefix = None
        self._page_horizontal_alignment = None
        self._page_margins = None
        self._resources_folder = None
        self._resources_folder_alias = None
        self._save_font_face_css_separately = None
        self._show_page_border = None
        self._use_target_machine_fonts = None
        self._save_format = "htmlfixed"
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
        if color_mode is not None:
            self.color_mode = color_mode
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if metafile_rendering_options is not None:
            self.metafile_rendering_options = metafile_rendering_options
        if numeral_format is not None:
            self.numeral_format = numeral_format
        if optimize_output is not None:
            self.optimize_output = optimize_output
        if page_count is not None:
            self.page_count = page_count
        if page_index is not None:
            self.page_index = page_index
        if css_class_names_prefix is not None:
            self.css_class_names_prefix = css_class_names_prefix
        if encoding is not None:
            self.encoding = encoding
        if export_embedded_css is not None:
            self.export_embedded_css = export_embedded_css
        if export_embedded_fonts is not None:
            self.export_embedded_fonts = export_embedded_fonts
        if export_embedded_images is not None:
            self.export_embedded_images = export_embedded_images
        if export_form_fields is not None:
            self.export_form_fields = export_form_fields
        if font_format is not None:
            self.font_format = font_format
        if id_prefix is not None:
            self.id_prefix = id_prefix
        if page_horizontal_alignment is not None:
            self.page_horizontal_alignment = page_horizontal_alignment
        if page_margins is not None:
            self.page_margins = page_margins
        if resources_folder is not None:
            self.resources_folder = resources_folder
        if resources_folder_alias is not None:
            self.resources_folder_alias = resources_folder_alias
        if save_font_face_css_separately is not None:
            self.save_font_face_css_separately = save_font_face_css_separately
        if show_page_border is not None:
            self.show_page_border = show_page_border
        if use_target_machine_fonts is not None:
            self.use_target_machine_fonts = use_target_machine_fonts

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this HtmlFixedSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this HtmlFixedSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this HtmlFixedSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
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
        """Gets the dml_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this HtmlFixedSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
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
        """Gets the dml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this HtmlFixedSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
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
        """Gets the file_name of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this HtmlFixedSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :return: The iml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this HtmlFixedSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
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
        """Gets the update_ambiguous_text_font of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :return: The update_ambiguous_text_font of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_ambiguous_text_font

    @update_ambiguous_text_font.setter
    def update_ambiguous_text_font(self, update_ambiguous_text_font):
        """Sets the update_ambiguous_text_font of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :param update_ambiguous_text_font: The update_ambiguous_text_font of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_ambiguous_text_font = update_ambiguous_text_font

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_created_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this HtmlFixedSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_last_saved_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def zip_output(self):
        """Gets the zip_output of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :return: The zip_output of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :param zip_output: The zip_output of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def color_mode(self):
        """Gets the color_mode of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}. The default value is Normal. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The color_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this HtmlFixedSaveOptionsData.

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}. The default value is Normal. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param color_mode: The color_mode of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Normal", "Grayscale"]  # noqa: E501
        if not color_mode.isdigit():
            if color_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(color_mode, allowed_values))
            self._color_mode = color_mode
        else:
            self._color_mode = allowed_values[int(color_mode) if six.PY3 else long(color_mode)]

    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this HtmlFixedSaveOptionsData.

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._jpeg_quality = jpeg_quality

    @property
    def metafile_rendering_options(self):
        """Gets the metafile_rendering_options of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the metafile rendering options.  # noqa: E501

        :return: The metafile_rendering_options of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: MetafileRenderingOptionsData
        """
        return self._metafile_rendering_options

    @metafile_rendering_options.setter
    def metafile_rendering_options(self, metafile_rendering_options):
        """Sets the metafile_rendering_options of this HtmlFixedSaveOptionsData.

        Gets or sets the metafile rendering options.  # noqa: E501

        :param metafile_rendering_options: The metafile_rendering_options of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: MetafileRenderingOptionsData
        """
        self._metafile_rendering_options = metafile_rendering_options

    @property
    def numeral_format(self):
        """Gets the numeral_format of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :return: The numeral_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._numeral_format

    @numeral_format.setter
    def numeral_format(self, numeral_format):
        """Sets the numeral_format of this HtmlFixedSaveOptionsData.

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :param numeral_format: The numeral_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["European", "ArabicIndic", "EasternArabicIndic", "Context", "System"]  # noqa: E501
        if not numeral_format.isdigit():
            if numeral_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `numeral_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(numeral_format, allowed_values))
            self._numeral_format = numeral_format
        else:
            self._numeral_format = allowed_values[int(numeral_format) if six.PY3 else long(numeral_format)]

    @property
    def optimize_output(self):
        """Gets the optimize_output of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :return: The optimize_output of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_output

    @optimize_output.setter
    def optimize_output(self, optimize_output):
        """Sets the optimize_output of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :param optimize_output: The optimize_output of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._optimize_output = optimize_output

    @property
    def page_count(self):
        """Gets the page_count of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the number of pages to render.  # noqa: E501

        :return: The page_count of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this HtmlFixedSaveOptionsData.

        Gets or sets the number of pages to render.  # noqa: E501

        :param page_count: The page_count of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_count = page_count

    @property
    def page_index(self):
        """Gets the page_index of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :return: The page_index of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this HtmlFixedSaveOptionsData.

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :param page_index: The page_index of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_index = page_index

    @property
    def css_class_names_prefix(self):
        """Gets the css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the prefix which is added to all class names in style.css file. The default value is "aw".  # noqa: E501

        :return: The css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_class_names_prefix

    @css_class_names_prefix.setter
    def css_class_names_prefix(self, css_class_names_prefix):
        """Sets the css_class_names_prefix of this HtmlFixedSaveOptionsData.

        Gets or sets the prefix which is added to all class names in style.css file. The default value is "aw".  # noqa: E501

        :param css_class_names_prefix: The css_class_names_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_class_names_prefix = css_class_names_prefix

    @property
    def encoding(self):
        """Gets the encoding of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the character encoding.  # noqa: E501

        :return: The encoding of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this HtmlFixedSaveOptionsData.

        Gets or sets the character encoding.  # noqa: E501

        :param encoding: The encoding of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding

    @property
    def export_embedded_css(self):
        """Gets the export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the CSS (Cascading Style Sheet) should be embedded into the Html document.  # noqa: E501

        :return: The export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_css

    @export_embedded_css.setter
    def export_embedded_css(self, export_embedded_css):
        """Sets the export_embedded_css of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether the CSS (Cascading Style Sheet) should be embedded into the Html document.  # noqa: E501

        :param export_embedded_css: The export_embedded_css of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_embedded_css = export_embedded_css

    @property
    def export_embedded_fonts(self):
        """Gets the export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fonts should be embedded into the Html document in Base64 format.  # noqa: E501

        :return: The export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_fonts

    @export_embedded_fonts.setter
    def export_embedded_fonts(self, export_embedded_fonts):
        """Sets the export_embedded_fonts of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether fonts should be embedded into the Html document in Base64 format.  # noqa: E501

        :param export_embedded_fonts: The export_embedded_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_embedded_fonts = export_embedded_fonts

    @property
    def export_embedded_images(self):
        """Gets the export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether images should be embedded into the Html document in Base64 format.  # noqa: E501

        :return: The export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_embedded_images

    @export_embedded_images.setter
    def export_embedded_images(self, export_embedded_images):
        """Sets the export_embedded_images of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether images should be embedded into the Html document in Base64 format.  # noqa: E501

        :param export_embedded_images: The export_embedded_images of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_embedded_images = export_embedded_images

    @property
    def export_form_fields(self):
        """Gets the export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether form fields are exported as interactive items (as 'input' tag) rather than converted to text or graphics.  # noqa: E501

        :return: The export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_form_fields

    @export_form_fields.setter
    def export_form_fields(self, export_form_fields):
        """Sets the export_form_fields of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether form fields are exported as interactive items (as 'input' tag) rather than converted to text or graphics.  # noqa: E501

        :param export_form_fields: The export_form_fields of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_form_fields = export_form_fields

    @property
    def font_format(self):
        """Gets the font_format of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the export format of fonts.  # noqa: E501

        :return: The font_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._font_format

    @font_format.setter
    def font_format(self, font_format):
        """Sets the font_format of this HtmlFixedSaveOptionsData.

        Gets or sets the export format of fonts.  # noqa: E501

        :param font_format: The font_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Woff", "Ttf"]  # noqa: E501
        if not font_format.isdigit():
            if font_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `font_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(font_format, allowed_values))
            self._font_format = font_format
        else:
            self._font_format = allowed_values[int(font_format) if six.PY3 else long(font_format)]

    @property
    def id_prefix(self):
        """Gets the id_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a prefix that is prepended to all generated element IDs in the output document. The default value is null and no prefix is prepended. If the prefix is specified, it can contain only letters, digits, underscores, and hyphens, and must start with a letter.  # noqa: E501

        :return: The id_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._id_prefix

    @id_prefix.setter
    def id_prefix(self, id_prefix):
        """Sets the id_prefix of this HtmlFixedSaveOptionsData.

        Gets or sets a prefix that is prepended to all generated element IDs in the output document. The default value is null and no prefix is prepended. If the prefix is specified, it can contain only letters, digits, underscores, and hyphens, and must start with a letter.  # noqa: E501

        :param id_prefix: The id_prefix of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._id_prefix = id_prefix

    @property
    def page_horizontal_alignment(self):
        """Gets the page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the horizontal alignment of pages in the HTML document. The default value is HtmlFixedHorizontalPageAlignment.Center.  # noqa: E501

        :return: The page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._page_horizontal_alignment

    @page_horizontal_alignment.setter
    def page_horizontal_alignment(self, page_horizontal_alignment):
        """Sets the page_horizontal_alignment of this HtmlFixedSaveOptionsData.

        Gets or sets the horizontal alignment of pages in the HTML document. The default value is HtmlFixedHorizontalPageAlignment.Center.  # noqa: E501

        :param page_horizontal_alignment: The page_horizontal_alignment of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Left", "Center", "Right"]  # noqa: E501
        if not page_horizontal_alignment.isdigit():
            if page_horizontal_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `page_horizontal_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(page_horizontal_alignment, allowed_values))
            self._page_horizontal_alignment = page_horizontal_alignment
        else:
            self._page_horizontal_alignment = allowed_values[int(page_horizontal_alignment) if six.PY3 else long(page_horizontal_alignment)]

    @property
    def page_margins(self):
        """Gets the page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the margin around pages in HTML document. The margins value is measured in points and should be equal to or greater than 0. The default value is 10 points. Depends on the value of PageHorizontalAlignment property: Defines top, bottom and left page margins if the value is Left. Defines top, bottom and right page margins if the value is Right. Defines top and bottom page margins if the value is Center.  # noqa: E501

        :return: The page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._page_margins

    @page_margins.setter
    def page_margins(self, page_margins):
        """Sets the page_margins of this HtmlFixedSaveOptionsData.

        Gets or sets the margin around pages in HTML document. The margins value is measured in points and should be equal to or greater than 0. The default value is 10 points. Depends on the value of PageHorizontalAlignment property: Defines top, bottom and left page margins if the value is Left. Defines top, bottom and right page margins if the value is Right. Defines top and bottom page margins if the value is Center.  # noqa: E501

        :param page_margins: The page_margins of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._page_margins = page_margins

    @property
    def resources_folder(self):
        """Gets the resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the physical folder where resources are saved when exporting the document.  # noqa: E501

        :return: The resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder

    @resources_folder.setter
    def resources_folder(self, resources_folder):
        """Sets the resources_folder of this HtmlFixedSaveOptionsData.

        Gets or sets the physical folder where resources are saved when exporting the document.  # noqa: E501

        :param resources_folder: The resources_folder of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resources_folder = resources_folder

    @property
    def resources_folder_alias(self):
        """Gets the resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets the name of the folder used to construct resource URIs.  # noqa: E501

        :return: The resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resources_folder_alias

    @resources_folder_alias.setter
    def resources_folder_alias(self, resources_folder_alias):
        """Sets the resources_folder_alias of this HtmlFixedSaveOptionsData.

        Gets or sets the name of the folder used to construct resource URIs.  # noqa: E501

        :param resources_folder_alias: The resources_folder_alias of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resources_folder_alias = resources_folder_alias

    @property
    def save_font_face_css_separately(self):
        """Gets the save_font_face_css_separately of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether "@font-face" CSS rules should be placed into a separate file "fontFaces.css" when a document is being saved with external stylesheet (that is, when Aspose.Words.Saving.HtmlFixedSaveOptions.ExportEmbeddedCss is false). The default value is false, all CSS rules are written into single file "styles.css". Setting this property to true restores the old behavior (separate files) for compatibility with legacy code.  # noqa: E501

        :return: The save_font_face_css_separately of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._save_font_face_css_separately

    @save_font_face_css_separately.setter
    def save_font_face_css_separately(self, save_font_face_css_separately):
        """Sets the save_font_face_css_separately of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether "@font-face" CSS rules should be placed into a separate file "fontFaces.css" when a document is being saved with external stylesheet (that is, when Aspose.Words.Saving.HtmlFixedSaveOptions.ExportEmbeddedCss is false). The default value is false, all CSS rules are written into single file "styles.css". Setting this property to true restores the old behavior (separate files) for compatibility with legacy code.  # noqa: E501

        :param save_font_face_css_separately: The save_font_face_css_separately of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._save_font_face_css_separately = save_font_face_css_separately

    @property
    def show_page_border(self):
        """Gets the show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to show border around pages.  # noqa: E501

        :return: The show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._show_page_border

    @show_page_border.setter
    def show_page_border(self, show_page_border):
        """Sets the show_page_border of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether to show border around pages.  # noqa: E501

        :param show_page_border: The show_page_border of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._show_page_border = show_page_border

    @property
    def use_target_machine_fonts(self):
        """Gets the use_target_machine_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fonts from target machine must be used to display the document. If this flag is set to true, Aspose.Words.Saving.HtmlFixedSaveOptions.FontFormat and Aspose.Words.Saving.HtmlFixedSaveOptions.ExportEmbeddedFonts properties do not have effect, also Aspose.Words.Saving.HtmlFixedSaveOptions.ResourceSavingCallback is not fired for fonts. The default value is false.  # noqa: E501

        :return: The use_target_machine_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_target_machine_fonts

    @use_target_machine_fonts.setter
    def use_target_machine_fonts(self, use_target_machine_fonts):
        """Sets the use_target_machine_fonts of this HtmlFixedSaveOptionsData.

        Gets or sets a value indicating whether fonts from target machine must be used to display the document. If this flag is set to true, Aspose.Words.Saving.HtmlFixedSaveOptions.FontFormat and Aspose.Words.Saving.HtmlFixedSaveOptions.ExportEmbeddedFonts properties do not have effect, also Aspose.Words.Saving.HtmlFixedSaveOptions.ResourceSavingCallback is not fired for fonts. The default value is false.  # noqa: E501

        :param use_target_machine_fonts: The use_target_machine_fonts of this HtmlFixedSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_target_machine_fonts = use_target_machine_fonts

    @property
    def save_format(self):
        """Gets the save_format of this HtmlFixedSaveOptionsData.  # noqa: E501

        Gets the format of save.  # noqa: E501

        :return: The save_format of this HtmlFixedSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format



    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._file_name is None:
            raise ValueError("Property FileName in HtmlFixedSaveOptionsData is required.")  # noqa: E501

        if self._custom_time_zone_info_data is not None:
            self._custom_time_zone_info_data.validate()
















        if self._metafile_rendering_options is not None:
            self._metafile_rendering_options.validate()






















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
        if not isinstance(other, HtmlFixedSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other