# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="emf_save_options_data.py">
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

class EmfSaveOptionsData(object):
    """Container class for emf save options.
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
        'horizontal_resolution': 'float',
        'image_brightness': 'float',
        'image_color_mode': 'str',
        'image_contrast': 'float',
        'paper_color': 'str',
        'pixel_format': 'str',
        'resolution': 'float',
        'scale': 'float',
        'use_anti_aliasing': 'bool',
        'use_high_quality_rendering': 'bool',
        'vertical_resolution': 'float',
        'image_height': 'int',
        'image_width': 'int',
        'use_gdi_emf_renderer': 'bool',
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
        'horizontal_resolution': 'HorizontalResolution',
        'image_brightness': 'ImageBrightness',
        'image_color_mode': 'ImageColorMode',
        'image_contrast': 'ImageContrast',
        'paper_color': 'PaperColor',
        'pixel_format': 'PixelFormat',
        'resolution': 'Resolution',
        'scale': 'Scale',
        'use_anti_aliasing': 'UseAntiAliasing',
        'use_high_quality_rendering': 'UseHighQualityRendering',
        'vertical_resolution': 'VerticalResolution',
        'image_height': 'ImageHeight',
        'image_width': 'ImageWidth',
        'use_gdi_emf_renderer': 'UseGdiEmfRenderer',
        'save_format': 'SaveFormat'
    }

    def __init__(self, allow_embedding_post_script_fonts=None, custom_time_zone_info_data=None, dml3_d_effects_rendering_mode=None, dml_effects_rendering_mode=None, dml_rendering_mode=None, file_name=None, iml_rendering_mode=None, update_ambiguous_text_font=None, update_created_time_property=None, update_fields=None, update_last_printed_property=None, update_last_saved_time_property=None, zip_output=None, color_mode=None, jpeg_quality=None, metafile_rendering_options=None, numeral_format=None, optimize_output=None, page_count=None, page_index=None, horizontal_resolution=None, image_brightness=None, image_color_mode=None, image_contrast=None, paper_color=None, pixel_format=None, resolution=None, scale=None, use_anti_aliasing=None, use_high_quality_rendering=None, vertical_resolution=None, image_height=None, image_width=None, use_gdi_emf_renderer=None):  # noqa: E501
        """EmfSaveOptionsData - a model defined in Swagger"""  # noqa: E501

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
        self._horizontal_resolution = None
        self._image_brightness = None
        self._image_color_mode = None
        self._image_contrast = None
        self._paper_color = None
        self._pixel_format = None
        self._resolution = None
        self._scale = None
        self._use_anti_aliasing = None
        self._use_high_quality_rendering = None
        self._vertical_resolution = None
        self._image_height = None
        self._image_width = None
        self._use_gdi_emf_renderer = None
        self._save_format = "emf"
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
        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if image_brightness is not None:
            self.image_brightness = image_brightness
        if image_color_mode is not None:
            self.image_color_mode = image_color_mode
        if image_contrast is not None:
            self.image_contrast = image_contrast
        if paper_color is not None:
            self.paper_color = paper_color
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if resolution is not None:
            self.resolution = resolution
        if scale is not None:
            self.scale = scale
        if use_anti_aliasing is not None:
            self.use_anti_aliasing = use_anti_aliasing
        if use_high_quality_rendering is not None:
            self.use_high_quality_rendering = use_high_quality_rendering
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution
        if image_height is not None:
            self.image_height = image_height
        if image_width is not None:
            self.image_width = image_width
        if use_gdi_emf_renderer is not None:
            self.use_gdi_emf_renderer = use_gdi_emf_renderer

    @property
    def allow_embedding_post_script_fonts(self):
        """Gets the allow_embedding_post_script_fonts of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :return: The allow_embedding_post_script_fonts of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._allow_embedding_post_script_fonts

    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, allow_embedding_post_script_fonts):
        """Sets the allow_embedding_post_script_fonts of this EmfSaveOptionsData.

        Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines when embedding TrueType fonts in a document upon it is saved. The default value is false.. Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type. This option only works when Aspose.Words.Fonts.FontInfoCollection.EmbedTrueTypeFonts of the Aspose.Words.DocumentBase.FontInfos property is set to true. The default value is false.  # noqa: E501

        :param allow_embedding_post_script_fonts: The allow_embedding_post_script_fonts of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._allow_embedding_post_script_fonts = allow_embedding_post_script_fonts

    @property
    def custom_time_zone_info_data(self):
        """Gets the custom_time_zone_info_data of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :return: The custom_time_zone_info_data of this EmfSaveOptionsData.  # noqa: E501
        :rtype: TimeZoneInfoData
        """
        return self._custom_time_zone_info_data

    @custom_time_zone_info_data.setter
    def custom_time_zone_info_data(self, custom_time_zone_info_data):
        """Sets the custom_time_zone_info_data of this EmfSaveOptionsData.

        Gets or sets CustomTimeZoneInfo.  # noqa: E501

        :param custom_time_zone_info_data: The custom_time_zone_info_data of this EmfSaveOptionsData.  # noqa: E501
        :type: TimeZoneInfoData
        """
        self._custom_time_zone_info_data = custom_time_zone_info_data

    @property
    def dml3_d_effects_rendering_mode(self):
        """Gets the dml3_d_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :return: The dml3_d_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml3_d_effects_rendering_mode

    @dml3_d_effects_rendering_mode.setter
    def dml3_d_effects_rendering_mode(self, dml3_d_effects_rendering_mode):
        """Sets the dml3_d_effects_rendering_mode of this EmfSaveOptionsData.

        Gets or sets the value determining how 3D effects are rendered. The default value is Aspose.Words.Saving.Dml3DEffectsRenderingMode.Basic.  # noqa: E501

        :param dml3_d_effects_rendering_mode: The dml3_d_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the dml_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_effects_rendering_mode

    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, dml_effects_rendering_mode):
        """Sets the dml_effects_rendering_mode of this EmfSaveOptionsData.

        Gets or sets the value determining how DrawingML effects are rendered. { Simplified | None | Fine }. The default value is Simplified. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_effects_rendering_mode: The dml_effects_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the dml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The dml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._dml_rendering_mode

    @dml_rendering_mode.setter
    def dml_rendering_mode(self, dml_rendering_mode):
        """Sets the dml_rendering_mode of this EmfSaveOptionsData.

        Gets or sets the option that controls how DrawingML shapes are rendered. { Fallback | DrawingML }. The default value is Fallback. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param dml_rendering_mode: The dml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the file_name of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the name of destination file.  # noqa: E501

        :return: The file_name of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this EmfSaveOptionsData.

        Gets or sets the name of destination file.  # noqa: E501

        :param file_name: The file_name of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def iml_rendering_mode(self):
        """Gets the iml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :return: The iml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._iml_rendering_mode

    @iml_rendering_mode.setter
    def iml_rendering_mode(self, iml_rendering_mode):
        """Sets the iml_rendering_mode of this EmfSaveOptionsData.

        Gets or sets the value determining how ink (InkML) objects are rendered. The default value is Aspose.Words.Saving.ImlRenderingMode.InkML.  # noqa: E501

        :param iml_rendering_mode: The iml_rendering_mode of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the update_ambiguous_text_font of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :return: The update_ambiguous_text_font of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_ambiguous_text_font

    @update_ambiguous_text_font.setter
    def update_ambiguous_text_font(self, update_ambiguous_text_font):
        """Sets the update_ambiguous_text_font of this EmfSaveOptionsData.

        Gets or sets a value indicating whether the font attributes will be changed according to the character code being used.  # noqa: E501

        :param update_ambiguous_text_font: The update_ambiguous_text_font of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_ambiguous_text_font = update_ambiguous_text_font

    @property
    def update_created_time_property(self):
        """Gets the update_created_time_property of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_created_time_property of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_created_time_property

    @update_created_time_property.setter
    def update_created_time_property(self, update_created_time_property):
        """Sets the update_created_time_property of this EmfSaveOptionsData.

        Gets or sets a value determining whether the Aspose.Words.Properties.BuiltInDocumentProperties.CreatedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_created_time_property: The update_created_time_property of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_created_time_property = update_created_time_property

    @property
    def update_fields(self):
        """Gets the update_fields of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :return: The update_fields of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_fields

    @update_fields.setter
    def update_fields(self, update_fields):
        """Sets the update_fields of this EmfSaveOptionsData.

        Gets or sets a value indicating whether fields should be updated before saving the document to a fixed page format. The default value is true.  # noqa: E501

        :param update_fields: The update_fields of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_fields = update_fields

    @property
    def update_last_printed_property(self):
        """Gets the update_last_printed_property of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :return: The update_last_printed_property of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_printed_property

    @update_last_printed_property.setter
    def update_last_printed_property(self, update_last_printed_property):
        """Sets the update_last_printed_property of this EmfSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastPrinted property is updated before saving.  # noqa: E501

        :param update_last_printed_property: The update_last_printed_property of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_printed_property = update_last_printed_property

    @property
    def update_last_saved_time_property(self):
        """Gets the update_last_saved_time_property of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :return: The update_last_saved_time_property of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._update_last_saved_time_property

    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, update_last_saved_time_property):
        """Sets the update_last_saved_time_property of this EmfSaveOptionsData.

        Gets or sets a value indicating whether the Aspose.Words.Properties.BuiltInDocumentProperties.LastSavedTime property is updated before saving. The default value is false.  # noqa: E501

        :param update_last_saved_time_property: The update_last_saved_time_property of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._update_last_saved_time_property = update_last_saved_time_property

    @property
    def zip_output(self):
        """Gets the zip_output of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :return: The zip_output of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._zip_output

    @zip_output.setter
    def zip_output(self, zip_output):
        """Sets the zip_output of this EmfSaveOptionsData.

        Gets or sets a value indicating whether to zip output or not. The default value is false. When set to true, output files will be zipped.  # noqa: E501

        :param zip_output: The zip_output of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._zip_output = zip_output

    @property
    def color_mode(self):
        """Gets the color_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}. The default value is Normal. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :return: The color_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this EmfSaveOptionsData.

        Gets or sets the value determining how colors are rendered. { Normal | Grayscale}. The default value is Normal. This property is used when the document is exported to fixed page formats.  # noqa: E501

        :param color_mode: The color_mode of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the jpeg_quality of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this EmfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this EmfSaveOptionsData.

        Gets or sets the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this EmfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._jpeg_quality = jpeg_quality

    @property
    def metafile_rendering_options(self):
        """Gets the metafile_rendering_options of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the metafile rendering options.  # noqa: E501

        :return: The metafile_rendering_options of this EmfSaveOptionsData.  # noqa: E501
        :rtype: MetafileRenderingOptionsData
        """
        return self._metafile_rendering_options

    @metafile_rendering_options.setter
    def metafile_rendering_options(self, metafile_rendering_options):
        """Sets the metafile_rendering_options of this EmfSaveOptionsData.

        Gets or sets the metafile rendering options.  # noqa: E501

        :param metafile_rendering_options: The metafile_rendering_options of this EmfSaveOptionsData.  # noqa: E501
        :type: MetafileRenderingOptionsData
        """
        self._metafile_rendering_options = metafile_rendering_options

    @property
    def numeral_format(self):
        """Gets the numeral_format of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :return: The numeral_format of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._numeral_format

    @numeral_format.setter
    def numeral_format(self, numeral_format):
        """Sets the numeral_format of this EmfSaveOptionsData.

        Gets or sets the symbol set, that is used to represent numbers while rendering to fixed page formats.  # noqa: E501

        :param numeral_format: The numeral_format of this EmfSaveOptionsData.  # noqa: E501
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
        """Gets the optimize_output of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :return: The optimize_output of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_output

    @optimize_output.setter
    def optimize_output(self, optimize_output):
        """Sets the optimize_output of this EmfSaveOptionsData.

        Gets or sets a value indicating whether it is required to optimize output of XPS. If this flag is set redundant nested canvases and empty canvases are removed, also neighbor glyphs with the same formatting are concatenated. Note: The accuracy of the content display may be affected if this property is set to true.. The default value is false.  # noqa: E501

        :param optimize_output: The optimize_output of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._optimize_output = optimize_output

    @property
    def page_count(self):
        """Gets the page_count of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the number of pages to render.  # noqa: E501

        :return: The page_count of this EmfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this EmfSaveOptionsData.

        Gets or sets the number of pages to render.  # noqa: E501

        :param page_count: The page_count of this EmfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_count = page_count

    @property
    def page_index(self):
        """Gets the page_index of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :return: The page_index of this EmfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this EmfSaveOptionsData.

        Gets or sets the 0-based index of the first page to render.  # noqa: E501

        :param page_index: The page_index of this EmfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._page_index = page_index

    @property
    def horizontal_resolution(self):
        """Gets the horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the horizontal resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """Sets the horizontal_resolution of this EmfSaveOptionsData.

        Gets or sets the horizontal resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param horizontal_resolution: The horizontal_resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._horizontal_resolution = horizontal_resolution

    @property
    def image_brightness(self):
        """Gets the image_brightness of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the brightness level of the image.  # noqa: E501

        :return: The image_brightness of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._image_brightness

    @image_brightness.setter
    def image_brightness(self, image_brightness):
        """Sets the image_brightness of this EmfSaveOptionsData.

        Gets or sets the brightness level of the image.  # noqa: E501

        :param image_brightness: The image_brightness of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._image_brightness = image_brightness

    @property
    def image_color_mode(self):
        """Gets the image_color_mode of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the color mode of the image.  # noqa: E501

        :return: The image_color_mode of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._image_color_mode

    @image_color_mode.setter
    def image_color_mode(self, image_color_mode):
        """Sets the image_color_mode of this EmfSaveOptionsData.

        Gets or sets the color mode of the image.  # noqa: E501

        :param image_color_mode: The image_color_mode of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Grayscale", "BlackAndWhite"]  # noqa: E501
        if not image_color_mode.isdigit():
            if image_color_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `image_color_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(image_color_mode, allowed_values))
            self._image_color_mode = image_color_mode
        else:
            self._image_color_mode = allowed_values[int(image_color_mode) if six.PY3 else long(image_color_mode)]

    @property
    def image_contrast(self):
        """Gets the image_contrast of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the contrast level of the image.  # noqa: E501

        :return: The image_contrast of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._image_contrast

    @image_contrast.setter
    def image_contrast(self, image_contrast):
        """Sets the image_contrast of this EmfSaveOptionsData.

        Gets or sets the contrast level of the image.  # noqa: E501

        :param image_contrast: The image_contrast of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._image_contrast = image_contrast

    @property
    def paper_color(self):
        """Gets the paper_color of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the background (paper) color of the image.  # noqa: E501

        :return: The paper_color of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._paper_color

    @paper_color.setter
    def paper_color(self, paper_color):
        """Sets the paper_color of this EmfSaveOptionsData.

        Gets or sets the background (paper) color of the image.  # noqa: E501

        :param paper_color: The paper_color of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        self._paper_color = paper_color

    @property
    def pixel_format(self):
        """Gets the pixel_format of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the pixel format of the image.  # noqa: E501

        :return: The pixel_format of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this EmfSaveOptionsData.

        Gets or sets the pixel format of the image.  # noqa: E501

        :param pixel_format: The pixel_format of this EmfSaveOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Format16BppRgb555", "Format16BppRgb565", "Format16BppArgb1555", "Format24BppRgb", "Format32BppRgb", "Format32BppArgb", "Format32BppPArgb", "Format48BppRgb", "Format64BppArgb", "Format64BppPArgb", "Format1bppIndexed"]  # noqa: E501
        if not pixel_format.isdigit():
            if pixel_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `pixel_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(pixel_format, allowed_values))
            self._pixel_format = pixel_format
        else:
            self._pixel_format = allowed_values[int(pixel_format) if six.PY3 else long(pixel_format)]

    @property
    def resolution(self):
        """Gets the resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets both horizontal and vertical resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this EmfSaveOptionsData.

        Gets or sets both horizontal and vertical resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param resolution: The resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._resolution = resolution

    @property
    def scale(self):
        """Gets the scale of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the zoom factor of the image.  # noqa: E501

        :return: The scale of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this EmfSaveOptionsData.

        Gets or sets the zoom factor of the image.  # noqa: E501

        :param scale: The scale of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._scale = scale

    @property
    def use_anti_aliasing(self):
        """Gets the use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use anti-aliasing for rendering.  # noqa: E501

        :return: The use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_anti_aliasing

    @use_anti_aliasing.setter
    def use_anti_aliasing(self, use_anti_aliasing):
        """Sets the use_anti_aliasing of this EmfSaveOptionsData.

        Gets or sets a value indicating whether to use anti-aliasing for rendering.  # noqa: E501

        :param use_anti_aliasing: The use_anti_aliasing of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_anti_aliasing = use_anti_aliasing

    @property
    def use_high_quality_rendering(self):
        """Gets the use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use high quality (i.e. slow) rendering algorithms.  # noqa: E501

        :return: The use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_high_quality_rendering

    @use_high_quality_rendering.setter
    def use_high_quality_rendering(self, use_high_quality_rendering):
        """Sets the use_high_quality_rendering of this EmfSaveOptionsData.

        Gets or sets a value indicating whether to use high quality (i.e. slow) rendering algorithms.  # noqa: E501

        :param use_high_quality_rendering: The use_high_quality_rendering of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_high_quality_rendering = use_high_quality_rendering

    @property
    def vertical_resolution(self):
        """Gets the vertical_resolution of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the vertical resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :return: The vertical_resolution of this EmfSaveOptionsData.  # noqa: E501
        :rtype: float
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """Sets the vertical_resolution of this EmfSaveOptionsData.

        Gets or sets the vertical resolution in dots per inch for the generated images. This property has effect only when saving to raster image formats. The default value is 96.  # noqa: E501

        :param vertical_resolution: The vertical_resolution of this EmfSaveOptionsData.  # noqa: E501
        :type: float
        """
        self._vertical_resolution = vertical_resolution

    @property
    def image_height(self):
        """Gets the image_height of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the height of a generated image in pixels. This property has effect only when saving to raster image formats and used in pair with ImageWidth.  # noqa: E501

        :return: The image_height of this EmfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this EmfSaveOptionsData.

        Gets or sets the height of a generated image in pixels. This property has effect only when saving to raster image formats and used in pair with ImageWidth.  # noqa: E501

        :param image_height: The image_height of this EmfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._image_height = image_height

    @property
    def image_width(self):
        """Gets the image_width of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets the width of a generated image in pixels. This property has effect only when saving to raster image formats and used in pair with ImageHeight.  # noqa: E501

        :return: The image_width of this EmfSaveOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this EmfSaveOptionsData.

        Gets or sets the width of a generated image in pixels. This property has effect only when saving to raster image formats and used in pair with ImageHeight.  # noqa: E501

        :param image_width: The image_width of this EmfSaveOptionsData.  # noqa: E501
        :type: int
        """
        self._image_width = image_width

    @property
    def use_gdi_emf_renderer(self):
        """Gets the use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501

        Gets or sets a value indicating whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF. If set to true - GDI+ metafile renderer is used. I.e. content is written to GDI+ graphics object and saved to metafile.If set to false - Aspose.Words metafile renderer is used. I.e. content is written directly to the metafile format with Aspose.Words.The default value is true.Has effect only when saving to EMF.  # noqa: E501

        :return: The use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_gdi_emf_renderer

    @use_gdi_emf_renderer.setter
    def use_gdi_emf_renderer(self, use_gdi_emf_renderer):
        """Sets the use_gdi_emf_renderer of this EmfSaveOptionsData.

        Gets or sets a value indicating whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF. If set to true - GDI+ metafile renderer is used. I.e. content is written to GDI+ graphics object and saved to metafile.If set to false - Aspose.Words metafile renderer is used. I.e. content is written directly to the metafile format with Aspose.Words.The default value is true.Has effect only when saving to EMF.  # noqa: E501

        :param use_gdi_emf_renderer: The use_gdi_emf_renderer of this EmfSaveOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_gdi_emf_renderer = use_gdi_emf_renderer

    @property
    def save_format(self):
        """Gets the save_format of this EmfSaveOptionsData.  # noqa: E501

        Gets the format of save.  # noqa: E501

        :return: The save_format of this EmfSaveOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._save_format



    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._file_name is None:
            raise ValueError("Property FileName in EmfSaveOptionsData is required.")  # noqa: E501

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
        if not isinstance(other, EmfSaveOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other