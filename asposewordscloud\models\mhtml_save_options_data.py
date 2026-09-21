# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="mhtml_save_options_data.py">
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

class MhtmlSaveOptionsData(object):
    """Container class for mhtml save options.
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
        'allow_negative_indent': 'bool',
        'css_class_name_prefix': 'str',
        'css_style_sheet_file_name': 'str',
        'css_style_sheet_type': 'str',
        'document_split_criteria': 'str',
        'document_split_heading_level': 'int',
        'encoding': 'str',
        'export_document_properties': 'bool',
        'export_drop_down_form_field_as_text': 'bool',
        'export_font_resources': 'bool',
        'export_fonts_as_base64': 'bool',
        'export_headers_footers_mode': 'str',
        'export_images_as_base64': 'bool',
        'export_language_information': 'bool',
        'export_list_labels': 'str',
        'export_original_url_for_linked_images': 'bool',
        'export_page_margins': 'bool',
        'export_page_setup': 'bool',
        'export_relative_font_size': 'bool',
        'export_roundtrip_information': 'bool',
        'export_text_input_form_field_as_text': 'bool',
        'export_toc_page_numbers': 'bool',
        'export_xhtml_transitional': 'bool',
        'font_resources_subsetting_size_threshold': 'int',
        'fonts_folder': 'str',
        'fonts_folder_alias': 'str',
        'html_version': 'str',
        'image_resolution': 'int',
        'images_folder': 'str',
        'images_folder_alias': 'str',
        'metafile_format': 'str',
        'office_math_output_mode': 'str',
        'pretty_format': 'bool',
        'remove_java_script_from_links': 'bool',
        'replace_backslash_with_yen_sign': 'bool',
        'resolve_font_names': 'bool',
        'resource_folder': 'str',
        'resource_folder_alias': 'str',
        'scale_image_to_shape_size': 'bool',
        'table_width_output_mode': 'str',
        'export_cid_urls_for_mhtml_resources': 'bool',
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
        'allow_negative_indent': 'AllowNegativeIndent',
        'css_class_name_prefix': 'CssClassNamePrefix',
        'css_style_sheet_file_name': 'CssStyleSheetFileName',
        'css_style_sheet_type': 'CssStyleSheetType',
        'document_split_criteria': 'DocumentSplitCriteria',
        'document_split_heading_level': 'DocumentSplitHeadingLevel',
        'encoding': 'Encoding',
        'export_document_properties': 'ExportDocumentProperties',
        'export_drop_down_form_field_as_text': 'ExportDropDownFormFieldAsText',
        'export_font_resources': 'ExportFontResources',
        'export_fonts_as_base64': 'ExportFontsAsBase64',
        'export_headers_footers_mode': 'ExportHeadersFootersMode',
        'export_images_as_base64': 'ExportImagesAsBase64',
        'export_language_information': 'ExportLanguageInformation',
        'export_list_labels': 'ExportListLabels',
        'export_original_url_for_linked_images': 'ExportOriginalUrlForLinkedImages',
        'export_page_margins': 'ExportPageMargins',
        'export_page_setup': 'ExportPageSetup',
        'export_relative_font_size': 'ExportRelativeFontSize',
        'export_roundtrip_information': 'ExportRoundtripInformation',
        'export_text_input_form_field_as_text': 'ExportTextInputFormFieldAsText',
        'export_toc_page_numbers': 'ExportTocPageNumbers',
        'export_xhtml_transitional': 'ExportXhtmlTransitional',
        'font_resources_subsetting_size_threshold': 'FontResourcesSubsettingSizeThreshold',
        'fonts_folder': 'FontsFolder',
        'fonts_folder_alias': 'FontsFolderAlias',
        'html_version': 'HtmlVersion',
        'image_resolution': 'ImageResolution',
        'images_folder': 'ImagesFolder',
        'images_folder_alias': 'ImagesFolderAlias',
        'metafile_format': 'MetafileFormat',
        'office_math_output_mode': 'OfficeMathOutputMode',
        'pretty_format': 'PrettyFormat',
        'remove_java_script_from_links': 'RemoveJavaScriptFromLinks',
        'replace_backslash_with_yen_sign': 'ReplaceBackslashWithYenSign',
        'resolve_font_names': 'ResolveFontNames',
        'resource_folder': 'ResourceFolder',
        'resource_folder_alias': 'ResourceFolderAlias',
        'scale_image_to_shape_size': 'ScaleImageToShapeSize',
        'table_width_output_mode': 'TableWidthOutputMode',
        'export_cid_urls_for_mhtml_resources': 'ExportCidUrlsForMhtmlResources',
        'save_format': 'SaveFormat'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, iml_rendering_mode=None, update_ambiguous_text_font=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, zip_output=None, allow_negative_indent=None, css_class_name_prefix=None, css_style_sheet_file_name=None, css_style_sheet_type=None, document_split_criteria=None, document_split_heading_level=None, encoding=None, export_document_properties=None, export_drop_down_form_field_as_text=None, export_font_resources=None, export_fonts_as_base64=None, export_headers_footers_mode=None, export_images_as_base64=None, export_language_information=None, export_list_labels=None, export_original_url_for_linked_images=None, export_page_margins=None, export_page_setup=None, export_relative_font_size=None, export_roundtrip_information=None, export_text_input_form_field_as_text=None, export_toc_page_numbers=None, export_xhtml_transitional=None, font_resources_subsetting_size_threshold=None, fonts_folder=None, fonts_folder_alias=None, html_version=None, image_resolution=None, images_folder=None, images_folder_alias=None, metafile_format=None, office_math_output_mode=None, pretty_format=None, remove_java_script_from_links=None, replace_backslash_with_yen_sign=None, resolve_font_names=None, resource_folder=None, resource_folder_alias=None, scale_image_to_shape_size=None, table_width_output_mode=None, export_cid_urls_for_mhtml_resources=None):  # noqa: E501
        """MhtmlSaveOptionsData - a model defined in Swagger"""  # noqa: E501

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
        self._allow_negative_indent = None
        self._css_class_name_prefix = None
        self._css_style_sheet_file_name = None
        self._css_style_sheet_type = None
        self._document_split_criteria = None
        self._document_split_heading_level = None
        self._encoding = None
        self._export_document_properties = None
        self._export_drop_down_form_field_as_text = None
        self._export_font_resources = None
        self._export_fonts_as_base64 = None
        self._export_headers_footers_mode = None
        self._export_images_as_base64 = None
        self._export_language_information = None
        self._export_list_labels = None
        self._export_original_url_for_linked_images = None
        self._export_page_margins = None
        self._export_page_setup = None
        self._export_relative_font_size = None
        self._export_roundtrip_information = None
        self._export_text_input_form_field_as_text = None
        self._export_toc_page_numbers = None
        self._export_xhtml_transitional = None
        self._font_resources_subsetting_size_threshold = None
        self._fonts_folder = None
        self._fonts_folder_alias = None
        self._html_version = None
        self._image_resolution = None
        self._images_folder = None
        self._images_folder_alias = None
        self._metafile_format = None
        self._office_math_output_mode = None
        self._pretty_format = None
        self._remove_java_script_from_links = None
        self._replace_backslash_with_yen_sign = None
        self._resolve_font_names = None
        self._resource_folder = None
        self._resource_folder_alias = None
        self._scale_image_to_shape_size = None
        self._table_width_output_mode = None
        self._export_cid_urls_for_mhtml_resources = None
        self._save_format = "mht"
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
        if allow_negative_indent is not None:
            self.allow_negative_indent = allow_negative_indent
        if css_class_name_prefix is not None:
            self.css_class_name_prefix = css_class_name_prefix
        if css_style_sheet_file_name is not None:
            self.css_style_sheet_file_name = css_style_sheet_file_name
        if css_style_sheet_type is not None:
            self.css_style_sheet_type = css_style_sheet_type
        if document_split_criteria is not None:
            self.document_split_criteria = document_split_criteria
        if document_split_heading_level is not None:
            self.document_split_heading_level = document_split_heading_level
        if encoding is not None:
            self.encoding = encoding
        if export_document_properties is not None:
            self.export_document_properties = export_document_properties
        if export_drop_down_form_field_as_text is not None:
            self.export_drop_down_form_field_as_text = export_drop_down_form_field_as_text
        if export_font_resources is not None:
            self.export_font_resources = export_font_resources
        if export_fonts_as_base64 is not None:
            self.export_fonts_as_base64 = export_fonts_as_base64
        if export_headers_footers_mode is not None:
            self.export_headers_footers_mode = export_headers_footers_mode
        if export_images_as_base64 is not None:
            self.export_images_as_base64 = export_images_as_base64
        if export_language_information is not None:
            self.export_language_information = export_language_information
        if export_list_labels is not None:
            self.export_list_labels = export_list_labels
        if export_original_url_for_linked_images is not None:
            self.export_original_url_for_linked_images = export_original_url_for_linked_images
        if export_page_margins is not None:
            self.export_page_margins = export_page_margins
        if export_page_setup is not None:
            self.export_page_setup = export_page_setup
        if export_relative_font_size is not None:
            self.export_relative_font_size = export_relative_font_size
        if export_roundtrip_information is not None:
            self.export_roundtrip_information = export_roundtrip_information
        if export_text_input_form_field_as_text is not None:
            self.export_text_input_form_field_as_text = export_text_input_form_field_as_text
        if export_toc_page_numbers is not None:
            self.export_toc_page_numbers = export_toc_page_numbers
        if export_xhtml_transitional is not None:
            self.export_xhtml_transitional = export_xhtml_transitional
        if font_resources_subsetting_size_threshold is not None:
            self.font_resources_subsetting_size_threshold = font_resources_subsetting_size_threshold
        if fonts_folder is not None:
            self.fonts_folder = fonts_folder
        if fonts_folder_alias is not None:
            self.fonts_folder_alias = fonts_folder_alias
        if html_version is not None:
            self.html_version = html_version
        if image_resolution is not None:
            self.image_resolution = image_resolution
        if images_folder is not None:
            self.images_folder = images_folder
        if images_folder_alias is not None:
            self.images_folder_alias = images_folder_alias
        if metafile_format is not None:
            self.metafile_format = metafile_format
        if office_math_output_mode is not None:
            self.office_math_output_mode = office_math_output_mode
        if pretty_format is not None:
            self.pretty_format = pretty_format
        if remove_java_script_from_links is not None:
            self.remove_java_script_from_links = remove_java_script_from_links
        if replace_backslash_with_yen_sign is not None:
            self.replace_backslash_with_yen_sign = replace_backslash_with_yen_sign
        if resolve_font_names is not None:
            self.resolve_font_names = resolve_font_names
        if resource_folder is not None:
            self.resource_folder = resource_folder
        if resource_folder_alias is not None:
            self.resource_folder_alias = resource_folder_alias
        if scale_image_to_shape_size is not None:
            self.scale_image_to_shape_size = scale_image_to_shape_size
        if table_width_output_mode is not None:
            self.table_width_output_mode = table_width_output_mode
        if export_cid_urls_for_mhtml_resources is not None:
            self.export_cid_urls_for_mhtml_resources = export_cid_urls_for_mhtml_resources

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this MhtmlSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this MhtmlSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this MhtmlSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this MhtmlSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
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
        """Gets the dml_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this MhtmlSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
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
        """Gets the dml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
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
        """Gets the file_name of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this MhtmlSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :return: The iml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this MhtmlSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this MhtmlSaveOptionsData.  # noqa: E501
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
        """Gets the update_ambiguous_text_font of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :return: The update_ambiguous_text_font of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_ambiguous_text_font

    @update_ambiguous_text_font.setter
    def update_ambiguous_text_font(self, update_ambiguous_text_font):
        """Sets the update_ambiguous_text_font of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :param update_ambiguous_text_font: The update_ambiguous_text_font of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_ambiguous_text_font = update_ambiguous_text_font

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_created_time_property of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this MhtmlSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_last_saved_time_property of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def zip_output(self):
        """Gets the zip_output of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :return: The zip_output of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :param zip_output: The zip_output of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def allow_negative_indent(self):
        """Gets the allow_negative_indent of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether negative left and right indents of paragraphs are allowed (not normalized).  # noqa: E501

        :return: The allow_negative_indent of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_negative_indent

    @allow_negative_indent.setter
    def allow_negative_indent(self, allow_negative_indent):
        """Sets the allow_negative_indent of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether negative left and right indents of paragraphs are allowed (not normalized).  # noqa: E501

        :param allow_negative_indent: The allow_negative_indent of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_negative_indent = allow_negative_indent

    @property
    def css_class_name_prefix(self):
        """Gets the css_class_name_prefix of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the prefix which is added to all CSS class names. The default value is an empty string and generated CSS class names have no common prefix. If this value is not empty, all CSS classes generated by Aspose.Words will start with the specified prefix.This might be useful, for example, if you add custom CSS to generated documents and want to prevent class name conflicts. If the value is not null or empty, it must be a valid CSS identifier.  # noqa: E501

        :return: The css_class_name_prefix of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_class_name_prefix

    @css_class_name_prefix.setter
    def css_class_name_prefix(self, css_class_name_prefix):
        """Sets the css_class_name_prefix of this MhtmlSaveOptionsData.

        Gets or sets the prefix which is added to all CSS class names. The default value is an empty string and generated CSS class names have no common prefix. If this value is not empty, all CSS classes generated by Aspose.Words will start with the specified prefix.This might be useful, for example, if you add custom CSS to generated documents and want to prevent class name conflicts. If the value is not null or empty, it must be a valid CSS identifier.  # noqa: E501

        :param css_class_name_prefix: The css_class_name_prefix of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_class_name_prefix = css_class_name_prefix

    @property
    def css_style_sheet_file_name(self):
        """Gets the css_style_sheet_file_name of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of the CSS file written when the document is exported to HTML.  # noqa: E501

        :return: The css_style_sheet_file_name of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_style_sheet_file_name

    @css_style_sheet_file_name.setter
    def css_style_sheet_file_name(self, css_style_sheet_file_name):
        """Sets the css_style_sheet_file_name of this MhtmlSaveOptionsData.

        Gets or sets the name of the CSS file written when the document is exported to HTML.  # noqa: E501

        :param css_style_sheet_file_name: The css_style_sheet_file_name of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._css_style_sheet_file_name = css_style_sheet_file_name

    @property
    def css_style_sheet_type(self):
        """Gets the css_style_sheet_type of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how the CSS styles are exported.  # noqa: E501

        :return: The css_style_sheet_type of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._css_style_sheet_type

    @css_style_sheet_type.setter
    def css_style_sheet_type(self, css_style_sheet_type):
        """Sets the css_style_sheet_type of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how the CSS styles are exported.  # noqa: E501

        :param css_style_sheet_type: The css_style_sheet_type of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Inline", "Embedded", "External"]  # noqa: E501
        if not css_style_sheet_type.isdigit():
            if css_style_sheet_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `css_style_sheet_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(css_style_sheet_type, allowed_values))
            self._css_style_sheet_type = css_style_sheet_type
        else:
            self._css_style_sheet_type = allowed_values[int(css_style_sheet_type) if six.PY3 else long(css_style_sheet_type)]

    @property
    def document_split_criteria(self):
        """Gets the document_split_criteria of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how the document should be split when saving.  # noqa: E501

        :return: The document_split_criteria of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._document_split_criteria

    @document_split_criteria.setter
    def document_split_criteria(self, document_split_criteria):
        """Sets the document_split_criteria of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how the document should be split when saving.  # noqa: E501

        :param document_split_criteria: The document_split_criteria of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "PageBreak", "ColumnBreak", "SectionBreak", "HeadingParagraph"]  # noqa: E501
        if not document_split_criteria.isdigit():
            if document_split_criteria not in allowed_values:
                raise ValueError(
                    "Invalid value for `document_split_criteria` ({0}), must be one of {1}"  # noqa: E501
                    .format(document_split_criteria, allowed_values))
            self._document_split_criteria = document_split_criteria
        else:
            self._document_split_criteria = allowed_values[int(document_split_criteria) if six.PY3 else long(document_split_criteria)]

    @property
    def document_split_heading_level(self):
        """Gets the document_split_heading_level of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the maximum level of headings at which to split the document.  # noqa: E501

        :return: The document_split_heading_level of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._document_split_heading_level

    @document_split_heading_level.setter
    def document_split_heading_level(self, document_split_heading_level):
        """Sets the document_split_heading_level of this MhtmlSaveOptionsData.

        Gets or sets the maximum level of headings at which to split the document.  # noqa: E501

        :param document_split_heading_level: The document_split_heading_level of this MhtmlSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._document_split_heading_level = document_split_heading_level

    @property
    def encoding(self):
        """Gets the encoding of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the character encoding to use when exporting.  # noqa: E501

        :return: The encoding of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this MhtmlSaveOptionsData.

        Gets or sets the character encoding to use when exporting.  # noqa: E501

        :param encoding: The encoding of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._encoding = encoding

    @property
    def export_document_properties(self):
        """Gets the export_document_properties of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to export built-in and custom document properties.  # noqa: E501

        :return: The export_document_properties of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_document_properties

    @export_document_properties.setter
    def export_document_properties(self, export_document_properties):
        """Sets the export_document_properties of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to export built-in and custom document properties.  # noqa: E501

        :param export_document_properties: The export_document_properties of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_document_properties = export_document_properties

    @property
    def export_drop_down_form_field_as_text(self):
        """Gets the export_drop_down_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the flag, that controls how drop-down form fields are saved to HTML. The default value is false. When set to true, exports drop-down form fields as normal text. When false, exports drop-down form fields as SELECT element in HTML.  # noqa: E501

        :return: The export_drop_down_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_drop_down_form_field_as_text

    @export_drop_down_form_field_as_text.setter
    def export_drop_down_form_field_as_text(self, export_drop_down_form_field_as_text):
        """Sets the export_drop_down_form_field_as_text of this MhtmlSaveOptionsData.

        Gets or sets the flag, that controls how drop-down form fields are saved to HTML. The default value is false. When set to true, exports drop-down form fields as normal text. When false, exports drop-down form fields as SELECT element in HTML.  # noqa: E501

        :param export_drop_down_form_field_as_text: The export_drop_down_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_drop_down_form_field_as_text = export_drop_down_form_field_as_text

    @property
    def export_font_resources(self):
        """Gets the export_font_resources of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether font resources should be exported.  # noqa: E501

        :return: The export_font_resources of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_font_resources

    @export_font_resources.setter
    def export_font_resources(self, export_font_resources):
        """Sets the export_font_resources of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether font resources should be exported.  # noqa: E501

        :param export_font_resources: The export_font_resources of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_font_resources = export_font_resources

    @property
    def export_fonts_as_base64(self):
        """Gets the export_fonts_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fonts resources should be embedded to HTML in Base64 encoding. The default value is false.  # noqa: E501

        :return: The export_fonts_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_fonts_as_base64

    @export_fonts_as_base64.setter
    def export_fonts_as_base64(self, export_fonts_as_base64):
        """Sets the export_fonts_as_base64 of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether fonts resources should be embedded to HTML in Base64 encoding. The default value is false.  # noqa: E501

        :param export_fonts_as_base64: The export_fonts_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_fonts_as_base64 = export_fonts_as_base64

    @property
    def export_headers_footers_mode(self):
        """Gets the export_headers_footers_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how headers and footers are exported.  # noqa: E501

        :return: The export_headers_footers_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_headers_footers_mode

    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, export_headers_footers_mode):
        """Sets the export_headers_footers_mode of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how headers and footers are exported.  # noqa: E501

        :param export_headers_footers_mode: The export_headers_footers_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "PerSection", "FirstSectionHeaderLastSectionFooter", "FirstPageHeaderFooterPerSection"]  # noqa: E501
        if not export_headers_footers_mode.isdigit():
            if export_headers_footers_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `export_headers_footers_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(export_headers_footers_mode, allowed_values))
            self._export_headers_footers_mode = export_headers_footers_mode
        else:
            self._export_headers_footers_mode = allowed_values[int(export_headers_footers_mode) if six.PY3 else long(export_headers_footers_mode)]

    @property
    def export_images_as_base64(self):
        """Gets the export_images_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether images are saved in Base64 format.  # noqa: E501

        :return: The export_images_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_images_as_base64

    @export_images_as_base64.setter
    def export_images_as_base64(self, export_images_as_base64):
        """Sets the export_images_as_base64 of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether images are saved in Base64 format.  # noqa: E501

        :param export_images_as_base64: The export_images_as_base64 of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_images_as_base64 = export_images_as_base64

    @property
    def export_language_information(self):
        """Gets the export_language_information of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether language information is exported.  # noqa: E501

        :return: The export_language_information of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_language_information

    @export_language_information.setter
    def export_language_information(self, export_language_information):
        """Sets the export_language_information of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether language information is exported.  # noqa: E501

        :param export_language_information: The export_language_information of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_language_information = export_language_information

    @property
    def export_list_labels(self):
        """Gets the export_list_labels of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how list labels are exported.  # noqa: E501

        :return: The export_list_labels of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._export_list_labels

    @export_list_labels.setter
    def export_list_labels(self, export_list_labels):
        """Sets the export_list_labels of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how list labels are exported.  # noqa: E501

        :param export_list_labels: The export_list_labels of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Auto", "AsInlineText", "ByHtmlTags"]  # noqa: E501
        if not export_list_labels.isdigit():
            if export_list_labels not in allowed_values:
                raise ValueError(
                    "Invalid value for `export_list_labels` ({0}), must be one of {1}"  # noqa: E501
                    .format(export_list_labels, allowed_values))
            self._export_list_labels = export_list_labels
        else:
            self._export_list_labels = allowed_values[int(export_list_labels) if six.PY3 else long(export_list_labels)]

    @property
    def export_original_url_for_linked_images(self):
        """Gets the export_original_url_for_linked_images of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the original URL should be used as the URL of the linked images. The default value is false. If value is set to true - ResourceFolder value is used as the URL of linked images and linked images are not loaded into document's folder or ImagesFolder.If value is set to false - linked images are loaded into document's folder or ImagesFolder and URL of each linked image is constructed depending on document's folder, ImagesFolder and ImagesFolderAlias properties.  # noqa: E501

        :return: The export_original_url_for_linked_images of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_original_url_for_linked_images

    @export_original_url_for_linked_images.setter
    def export_original_url_for_linked_images(self, export_original_url_for_linked_images):
        """Sets the export_original_url_for_linked_images of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether the original URL should be used as the URL of the linked images. The default value is false. If value is set to true - ResourceFolder value is used as the URL of linked images and linked images are not loaded into document's folder or ImagesFolder.If value is set to false - linked images are loaded into document's folder or ImagesFolder and URL of each linked image is constructed depending on document's folder, ImagesFolder and ImagesFolderAlias properties.  # noqa: E501

        :param export_original_url_for_linked_images: The export_original_url_for_linked_images of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_original_url_for_linked_images = export_original_url_for_linked_images

    @property
    def export_page_margins(self):
        """Gets the export_page_margins of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether page margins are exported to HTML, MHTML or EPUB. The default value is false. Aspose.Words does not show the area of page margins by default. If any elements are completely or partially clipped by the document edge the displayed area can be extended with this option.  # noqa: E501

        :return: The export_page_margins of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_page_margins

    @export_page_margins.setter
    def export_page_margins(self, export_page_margins):
        """Sets the export_page_margins of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether page margins are exported to HTML, MHTML or EPUB. The default value is false. Aspose.Words does not show the area of page margins by default. If any elements are completely or partially clipped by the document edge the displayed area can be extended with this option.  # noqa: E501

        :param export_page_margins: The export_page_margins of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_page_margins = export_page_margins

    @property
    def export_page_setup(self):
        """Gets the export_page_setup of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether page setup is exported.  # noqa: E501

        :return: The export_page_setup of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_page_setup

    @export_page_setup.setter
    def export_page_setup(self, export_page_setup):
        """Sets the export_page_setup of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether page setup is exported.  # noqa: E501

        :param export_page_setup: The export_page_setup of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_page_setup = export_page_setup

    @property
    def export_relative_font_size(self):
        """Gets the export_relative_font_size of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether font sizes should be output in relative units when saving.  # noqa: E501

        :return: The export_relative_font_size of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_relative_font_size

    @export_relative_font_size.setter
    def export_relative_font_size(self, export_relative_font_size):
        """Sets the export_relative_font_size of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether font sizes should be output in relative units when saving.  # noqa: E501

        :param export_relative_font_size: The export_relative_font_size of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_relative_font_size = export_relative_font_size

    @property
    def export_roundtrip_information(self):
        """Gets the export_roundtrip_information of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to write the roundtrip information when saving to HTML. The default value is true. Saving of the roundtrip information allows to restore document properties such as tab stops, comments, headers and footers during the HTML documents loading back into a Document object.When true, the roundtrip information is exported as -aw-* CSS properties of the corresponding HTML elements.When false, causes no roundtrip information to be output into produced files.  # noqa: E501

        :return: The export_roundtrip_information of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_roundtrip_information

    @export_roundtrip_information.setter
    def export_roundtrip_information(self, export_roundtrip_information):
        """Sets the export_roundtrip_information of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to write the roundtrip information when saving to HTML. The default value is true. Saving of the roundtrip information allows to restore document properties such as tab stops, comments, headers and footers during the HTML documents loading back into a Document object.When true, the roundtrip information is exported as -aw-* CSS properties of the corresponding HTML elements.When false, causes no roundtrip information to be output into produced files.  # noqa: E501

        :param export_roundtrip_information: The export_roundtrip_information of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_roundtrip_information = export_roundtrip_information

    @property
    def export_text_input_form_field_as_text(self):
        """Gets the export_text_input_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the flag, that controls how text input form fields are saved.  # noqa: E501

        :return: The export_text_input_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_text_input_form_field_as_text

    @export_text_input_form_field_as_text.setter
    def export_text_input_form_field_as_text(self, export_text_input_form_field_as_text):
        """Sets the export_text_input_form_field_as_text of this MhtmlSaveOptionsData.

        Gets or sets the flag, that controls how text input form fields are saved.  # noqa: E501

        :param export_text_input_form_field_as_text: The export_text_input_form_field_as_text of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_text_input_form_field_as_text = export_text_input_form_field_as_text

    @property
    def export_toc_page_numbers(self):
        """Gets the export_toc_page_numbers of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to write page numbers to table of contents when saving.  # noqa: E501

        :return: The export_toc_page_numbers of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_toc_page_numbers

    @export_toc_page_numbers.setter
    def export_toc_page_numbers(self, export_toc_page_numbers):
        """Sets the export_toc_page_numbers of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to write page numbers to table of contents when saving.  # noqa: E501

        :param export_toc_page_numbers: The export_toc_page_numbers of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_toc_page_numbers = export_toc_page_numbers

    @property
    def export_xhtml_transitional(self):
        """Gets the export_xhtml_transitional of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to write the DOCTYPE declaration when saving.  # noqa: E501

        :return: The export_xhtml_transitional of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_xhtml_transitional

    @export_xhtml_transitional.setter
    def export_xhtml_transitional(self, export_xhtml_transitional):
        """Sets the export_xhtml_transitional of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to write the DOCTYPE declaration when saving.  # noqa: E501

        :param export_xhtml_transitional: The export_xhtml_transitional of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_xhtml_transitional = export_xhtml_transitional

    @property
    def font_resources_subsetting_size_threshold(self):
        """Gets the font_resources_subsetting_size_threshold of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls which font resources need subsetting when saving.  # noqa: E501

        :return: The font_resources_subsetting_size_threshold of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._font_resources_subsetting_size_threshold

    @font_resources_subsetting_size_threshold.setter
    def font_resources_subsetting_size_threshold(self, font_resources_subsetting_size_threshold):
        """Sets the font_resources_subsetting_size_threshold of this MhtmlSaveOptionsData.

        Gets or sets the option that controls which font resources need subsetting when saving.  # noqa: E501

        :param font_resources_subsetting_size_threshold: The font_resources_subsetting_size_threshold of this MhtmlSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._font_resources_subsetting_size_threshold = font_resources_subsetting_size_threshold

    @property
    def fonts_folder(self):
        """Gets the fonts_folder of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the physical folder where fonts are saved when exporting a document.  # noqa: E501

        :return: The fonts_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._fonts_folder

    @fonts_folder.setter
    def fonts_folder(self, fonts_folder):
        """Sets the fonts_folder of this MhtmlSaveOptionsData.

        Gets or sets the physical folder where fonts are saved when exporting a document.  # noqa: E501

        :param fonts_folder: The fonts_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._fonts_folder = fonts_folder

    @property
    def fonts_folder_alias(self):
        """Gets the fonts_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of the folder used to construct font URIs.  # noqa: E501

        :return: The fonts_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._fonts_folder_alias

    @fonts_folder_alias.setter
    def fonts_folder_alias(self, fonts_folder_alias):
        """Sets the fonts_folder_alias of this MhtmlSaveOptionsData.

        Gets or sets the name of the folder used to construct font URIs.  # noqa: E501

        :param fonts_folder_alias: The fonts_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._fonts_folder_alias = fonts_folder_alias

    @property
    def html_version(self):
        """Gets the html_version of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the version of HTML standard, that should be used when saving the document to HTML or MHTML. The default value is Aspose.Words.Saving.HtmlVersion.Xhtml.  # noqa: E501

        :return: The html_version of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._html_version

    @html_version.setter
    def html_version(self, html_version):
        """Sets the html_version of this MhtmlSaveOptionsData.

        Gets or sets the version of HTML standard, that should be used when saving the document to HTML or MHTML. The default value is Aspose.Words.Saving.HtmlVersion.Xhtml.  # noqa: E501

        :param html_version: The html_version of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Xhtml", "Html5"]  # noqa: E501
        if not html_version.isdigit():
            if html_version not in allowed_values:
                raise ValueError(
                    "Invalid value for `html_version` ({0}), must be one of {1}"  # noqa: E501
                    .format(html_version, allowed_values))
            self._html_version = html_version
        else:
            self._html_version = allowed_values[int(html_version) if six.PY3 else long(html_version)]

    @property
    def image_resolution(self):
        """Gets the image_resolution of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the output resolution for images when exporting.  # noqa: E501

        :return: The image_resolution of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._image_resolution

    @image_resolution.setter
    def image_resolution(self, image_resolution):
        """Sets the image_resolution of this MhtmlSaveOptionsData.

        Gets or sets the output resolution for images when exporting.  # noqa: E501

        :param image_resolution: The image_resolution of this MhtmlSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._image_resolution = image_resolution

    @property
    def images_folder(self):
        """Gets the images_folder of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the physical folder where images are saved when exporting a document.  # noqa: E501

        :return: The images_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder

    @images_folder.setter
    def images_folder(self, images_folder):
        """Sets the images_folder of this MhtmlSaveOptionsData.

        Gets or sets the physical folder where images are saved when exporting a document.  # noqa: E501

        :param images_folder: The images_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._images_folder = images_folder

    @property
    def images_folder_alias(self):
        """Gets the images_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of the folder used to construct image URIs.  # noqa: E501

        :return: The images_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._images_folder_alias

    @images_folder_alias.setter
    def images_folder_alias(self, images_folder_alias):
        """Sets the images_folder_alias of this MhtmlSaveOptionsData.

        Gets or sets the name of the folder used to construct image URIs.  # noqa: E501

        :param images_folder_alias: The images_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._images_folder_alias = images_folder_alias

    @property
    def metafile_format(self):
        """Gets the metafile_format of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the options, that controls in what format metafiles are saved when exporting to HTML, MHTML, or EPUB. The default value is Aspose.Words.Saving.HtmlMetafileFormat.Png, meaning that metafiles are rendered to raster PNG images. Metafiles are not natively displayed by HTML browsers. By default, Aspose.Words converts WMF and EMF images into PNG files when exporting to HTML.Other options are to convert metafiles to SVG images or to export them as is without conversion. Some image transforms, in particular image cropping, will not be applied to metafile images if they are exported to HTML without conversion.  # noqa: E501

        :return: The metafile_format of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._metafile_format

    @metafile_format.setter
    def metafile_format(self, metafile_format):
        """Sets the metafile_format of this MhtmlSaveOptionsData.

        Gets or sets the options, that controls in what format metafiles are saved when exporting to HTML, MHTML, or EPUB. The default value is Aspose.Words.Saving.HtmlMetafileFormat.Png, meaning that metafiles are rendered to raster PNG images. Metafiles are not natively displayed by HTML browsers. By default, Aspose.Words converts WMF and EMF images into PNG files when exporting to HTML.Other options are to convert metafiles to SVG images or to export them as is without conversion. Some image transforms, in particular image cropping, will not be applied to metafile images if they are exported to HTML without conversion.  # noqa: E501

        :param metafile_format: The metafile_format of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Png", "Svg", "EmfOrWmf"]  # noqa: E501
        if not metafile_format.isdigit():
            if metafile_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `metafile_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(metafile_format, allowed_values))
            self._metafile_format = metafile_format
        else:
            self._metafile_format = allowed_values[int(metafile_format) if six.PY3 else long(metafile_format)]

    @property
    def office_math_output_mode(self):
        """Gets the office_math_output_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how OfficeMath objects are exported to HTML, MHTML or EPUB. The default value is HtmlOfficeMathOutputMode.Image.  # noqa: E501

        :return: The office_math_output_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._office_math_output_mode

    @office_math_output_mode.setter
    def office_math_output_mode(self, office_math_output_mode):
        """Sets the office_math_output_mode of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how OfficeMath objects are exported to HTML, MHTML or EPUB. The default value is HtmlOfficeMathOutputMode.Image.  # noqa: E501

        :param office_math_output_mode: The office_math_output_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Image", "MathML", "Text"]  # noqa: E501
        if not office_math_output_mode.isdigit():
            if office_math_output_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `office_math_output_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(office_math_output_mode, allowed_values))
            self._office_math_output_mode = office_math_output_mode
        else:
            self._office_math_output_mode = allowed_values[int(office_math_output_mode) if six.PY3 else long(office_math_output_mode)]

    @property
    def pretty_format(self):
        """Gets the pretty_format of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use pretty formats output.  # noqa: E501

        :return: The pretty_format of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._pretty_format

    @pretty_format.setter
    def pretty_format(self, pretty_format):
        """Sets the pretty_format of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to use pretty formats output.  # noqa: E501

        :param pretty_format: The pretty_format of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._pretty_format = pretty_format

    @property
    def remove_java_script_from_links(self):
        """Gets the remove_java_script_from_links of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the flag that indicates whether JavaScript will be removed from links. Default is false. If this option is enabled, all links containing JavaScript (e.g., links with "javascript:" in the href attribute) will be replaced with "javascript:void(0)". This can help prevent potential security risks, such as XSS attacks.  # noqa: E501

        :return: The remove_java_script_from_links of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._remove_java_script_from_links

    @remove_java_script_from_links.setter
    def remove_java_script_from_links(self, remove_java_script_from_links):
        """Sets the remove_java_script_from_links of this MhtmlSaveOptionsData.

        Gets or sets the flag that indicates whether JavaScript will be removed from links. Default is false. If this option is enabled, all links containing JavaScript (e.g., links with "javascript:" in the href attribute) will be replaced with "javascript:void(0)". This can help prevent potential security risks, such as XSS attacks.  # noqa: E501

        :param remove_java_script_from_links: The remove_java_script_from_links of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._remove_java_script_from_links = remove_java_script_from_links

    @property
    def replace_backslash_with_yen_sign(self):
        """Gets the replace_backslash_with_yen_sign of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the flag that indicates whether backslash characters should be replaced with yen signs. The default value is false. By default, Aspose.Words mimics MS Word's behavior and doesn't replace backslash characters with yen signs in generated HTML documents. However, previous versions of Aspose.Words performed such replacements in certain scenarios. This flag enables backward compatibility with previous versions of Aspose.Words.  # noqa: E501

        :return: The replace_backslash_with_yen_sign of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._replace_backslash_with_yen_sign

    @replace_backslash_with_yen_sign.setter
    def replace_backslash_with_yen_sign(self, replace_backslash_with_yen_sign):
        """Sets the replace_backslash_with_yen_sign of this MhtmlSaveOptionsData.

        Gets or sets the flag that indicates whether backslash characters should be replaced with yen signs. The default value is false. By default, Aspose.Words mimics MS Word's behavior and doesn't replace backslash characters with yen signs in generated HTML documents. However, previous versions of Aspose.Words performed such replacements in certain scenarios. This flag enables backward compatibility with previous versions of Aspose.Words.  # noqa: E501

        :param replace_backslash_with_yen_sign: The replace_backslash_with_yen_sign of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._replace_backslash_with_yen_sign = replace_backslash_with_yen_sign

    @property
    def resolve_font_names(self):
        """Gets the resolve_font_names of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether font family names used in the document are resolved and substituted according to FontSettings when being written into HTML-based formats. The default value is false.  # noqa: E501

        :return: The resolve_font_names of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._resolve_font_names

    @resolve_font_names.setter
    def resolve_font_names(self, resolve_font_names):
        """Sets the resolve_font_names of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether font family names used in the document are resolved and substituted according to FontSettings when being written into HTML-based formats. The default value is false.  # noqa: E501

        :param resolve_font_names: The resolve_font_names of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._resolve_font_names = resolve_font_names

    @property
    def resource_folder(self):
        """Gets the resource_folder of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the physical folder where all resources like images, fonts, and external CSS are saved when a document is exported to HTML. The default value is an empty string.  # noqa: E501

        :return: The resource_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_folder

    @resource_folder.setter
    def resource_folder(self, resource_folder):
        """Sets the resource_folder of this MhtmlSaveOptionsData.

        Gets or sets the physical folder where all resources like images, fonts, and external CSS are saved when a document is exported to HTML. The default value is an empty string.  # noqa: E501

        :param resource_folder: The resource_folder of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resource_folder = resource_folder

    @property
    def resource_folder_alias(self):
        """Gets the resource_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the name of the folder used to construct URIs of all resources written into HTML document. The default value is an empty string.  # noqa: E501

        :return: The resource_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_folder_alias

    @resource_folder_alias.setter
    def resource_folder_alias(self, resource_folder_alias):
        """Sets the resource_folder_alias of this MhtmlSaveOptionsData.

        Gets or sets the name of the folder used to construct URIs of all resources written into HTML document. The default value is an empty string.  # noqa: E501

        :param resource_folder_alias: The resource_folder_alias of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._resource_folder_alias = resource_folder_alias

    @property
    def scale_image_to_shape_size(self):
        """Gets the scale_image_to_shape_size of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether images are scaled by Aspose.Words to the bounding shape size when exporting.  # noqa: E501

        :return: The scale_image_to_shape_size of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._scale_image_to_shape_size

    @scale_image_to_shape_size.setter
    def scale_image_to_shape_size(self, scale_image_to_shape_size):
        """Sets the scale_image_to_shape_size of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether images are scaled by Aspose.Words to the bounding shape size when exporting.  # noqa: E501

        :param scale_image_to_shape_size: The scale_image_to_shape_size of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._scale_image_to_shape_size = scale_image_to_shape_size

    @property
    def table_width_output_mode(self):
        """Gets the table_width_output_mode of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how table, row and cell widths are exported.  # noqa: E501

        :return: The table_width_output_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._table_width_output_mode

    @table_width_output_mode.setter
    def table_width_output_mode(self, table_width_output_mode):
        """Sets the table_width_output_mode of this MhtmlSaveOptionsData.

        Gets or sets the option that controls how table, row and cell widths are exported.  # noqa: E501

        :param table_width_output_mode: The table_width_output_mode of this MhtmlSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["All", "RelativeOnly", "None"]  # noqa: E501
        if not table_width_output_mode.isdigit():
            if table_width_output_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `table_width_output_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(table_width_output_mode, allowed_values))
            self._table_width_output_mode = table_width_output_mode
        else:
            self._table_width_output_mode = allowed_values[int(table_width_output_mode) if six.PY3 else long(table_width_output_mode)]

    @property
    def export_cid_urls_for_mhtml_resources(self):
        """Gets the export_cid_urls_for_mhtml_resources of this MhtmlSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use CID (Content-ID) URLs to reference resources (images, fonts, CSS) included in MHTML documents. The default value is false. By default, resources in MHTML documents are referenced by file name (for example, "image.png"), which are matched against "Content-Location" headers of MIME parts. This option enables an alternative method, where references to resource files are written as CID (Content-ID) URLs (for example, "cid:image.png") and are matched against "Content-ID" headers. In theory, there should be no difference between the two referencing methods and either of them should work fine in any browser or mail agent. In practice, however, some agents fail to fetch resources by file name. If your browser or mail agent refuses to load resources included in an MTHML document (doesn't show images or doesn't load CSS styles), try exporting the document with CID URLs.  # noqa: E501

        :return: The export_cid_urls_for_mhtml_resources of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._export_cid_urls_for_mhtml_resources

    @export_cid_urls_for_mhtml_resources.setter
    def export_cid_urls_for_mhtml_resources(self, export_cid_urls_for_mhtml_resources):
        """Sets the export_cid_urls_for_mhtml_resources of this MhtmlSaveOptionsData.

        Gets or sets a value indicating whether to use CID (Content-ID) URLs to reference resources (images, fonts, CSS) included in MHTML documents. The default value is false. By default, resources in MHTML documents are referenced by file name (for example, "image.png"), which are matched against "Content-Location" headers of MIME parts. This option enables an alternative method, where references to resource files are written as CID (Content-ID) URLs (for example, "cid:image.png") and are matched against "Content-ID" headers. In theory, there should be no difference between the two referencing methods and either of them should work fine in any browser or mail agent. In practice, however, some agents fail to fetch resources by file name. If your browser or mail agent refuses to load resources included in an MTHML document (doesn't show images or doesn't load CSS styles), try exporting the document with CID URLs.  # noqa: E501

        :param export_cid_urls_for_mhtml_resources: The export_cid_urls_for_mhtml_resources of this MhtmlSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._export_cid_urls_for_mhtml_resources = export_cid_urls_for_mhtml_resources

    @property
    def save_format(self):
        """Gets the save_format of this MhtmlSaveOptionsData.  # noqa: E501

        Gets the format of save.  # noqa: E501

        :return: The save_format of this MhtmlSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format



    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._file_name is None:
            raise ValueError("Property FileName in MhtmlSaveOptionsData is required.")  # noqa: E501

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
        if not isinstance(other, MhtmlSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other