# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="metafile_rendering_options_data.py">
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

class MetafileRenderingOptionsData(object):
    """Container class for options of metafile rendering.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'emf_plus_dual_rendering_mode': 'str',
        'emulate_raster_operations': 'bool',
        'emulate_rendering_to_size_on_page': 'bool',
        'emulate_rendering_to_size_on_page_resolution': 'int',
        'rendering_mode': 'str',
        'use_emf_embedded_to_wmf': 'bool'
    }

    attribute_map = {
        'emf_plus_dual_rendering_mode': 'EmfPlusDualRenderingMode',
        'emulate_raster_operations': 'EmulateRasterOperations',
        'emulate_rendering_to_size_on_page': 'EmulateRenderingToSizeOnPage',
        'emulate_rendering_to_size_on_page_resolution': 'EmulateRenderingToSizeOnPageResolution',
        'rendering_mode': 'RenderingMode',
        'use_emf_embedded_to_wmf': 'UseEmfEmbeddedToWmf'
    }

    def __init__(self, emf_plus_dual_rendering_mode=None, emulate_raster_operations=None, emulate_rendering_to_size_on_page=None, emulate_rendering_to_size_on_page_resolution=None, rendering_mode=None, use_emf_embedded_to_wmf=None):  # noqa: E501
        """MetafileRenderingOptionsData - a model defined in Swagger"""  # noqa: E501

        self._emf_plus_dual_rendering_mode = None
        self._emulate_raster_operations = None
        self._emulate_rendering_to_size_on_page = None
        self._emulate_rendering_to_size_on_page_resolution = None
        self._rendering_mode = None
        self._use_emf_embedded_to_wmf = None
        self.discriminator = None

        if emf_plus_dual_rendering_mode is not None:
            self.emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
        if emulate_raster_operations is not None:
            self.emulate_raster_operations = emulate_raster_operations
        if emulate_rendering_to_size_on_page is not None:
            self.emulate_rendering_to_size_on_page = emulate_rendering_to_size_on_page
        if emulate_rendering_to_size_on_page_resolution is not None:
            self.emulate_rendering_to_size_on_page_resolution = emulate_rendering_to_size_on_page_resolution
        if rendering_mode is not None:
            self.rendering_mode = rendering_mode
        if use_emf_embedded_to_wmf is not None:
            self.use_emf_embedded_to_wmf = use_emf_embedded_to_wmf

    @property
    def emf_plus_dual_rendering_mode(self):
        """Gets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the option that controls how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :return: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._emf_plus_dual_rendering_mode

    @emf_plus_dual_rendering_mode.setter
    def emf_plus_dual_rendering_mode(self, emf_plus_dual_rendering_mode):
        """Sets the emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets the option that controls how EMF+ Dual metafiles should be rendered.  # noqa: E501

        :param emf_plus_dual_rendering_mode: The emf_plus_dual_rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["EmfPlusWithFallback", "EmfPlus", "Emf"]  # noqa: E501
        if not emf_plus_dual_rendering_mode.isdigit():
            if emf_plus_dual_rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `emf_plus_dual_rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(emf_plus_dual_rendering_mode, allowed_values))
            self._emf_plus_dual_rendering_mode = emf_plus_dual_rendering_mode
        else:
            self._emf_plus_dual_rendering_mode = allowed_values[int(emf_plus_dual_rendering_mode) if six.PY3 else long(emf_plus_dual_rendering_mode)]

    @property
    def emulate_raster_operations(self):
        """Gets the emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value indicating whether the raster operations should be emulated. Specific raster operations could be used in metafiles. They can not be rendered directly to vector graphics. Emulating raster operations requires partial rasterization of the resulting vector graphics which may affect the metafile rendering performance. When this value is set to true, Aspose.Words emulates the raster operations. The resulting output maybe partially rasterized and performance might be slower. When this value is set to false, Aspose.Words does not emulate the raster operations. When Aspose.Words encounters a raster operation in a metafile it fallbacks to rendering the metafile into a bitmap by using the operating system. This option is used only when metafile is rendered as vector graphics. The default value is true.  # noqa: E501

        :return: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._emulate_raster_operations

    @emulate_raster_operations.setter
    def emulate_raster_operations(self, emulate_raster_operations):
        """Sets the emulate_raster_operations of this MetafileRenderingOptionsData.

        Gets or sets a value indicating whether the raster operations should be emulated. Specific raster operations could be used in metafiles. They can not be rendered directly to vector graphics. Emulating raster operations requires partial rasterization of the resulting vector graphics which may affect the metafile rendering performance. When this value is set to true, Aspose.Words emulates the raster operations. The resulting output maybe partially rasterized and performance might be slower. When this value is set to false, Aspose.Words does not emulate the raster operations. When Aspose.Words encounters a raster operation in a metafile it fallbacks to rendering the metafile into a bitmap by using the operating system. This option is used only when metafile is rendered as vector graphics. The default value is true.  # noqa: E501

        :param emulate_raster_operations: The emulate_raster_operations of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._emulate_raster_operations = emulate_raster_operations

    @property
    def emulate_rendering_to_size_on_page(self):
        """Gets the emulate_rendering_to_size_on_page of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets a value determining whether metafile rendering emulates the display of the metafile according to the size on page or the display of the metafile in its default size.  # noqa: E501

        :return: The emulate_rendering_to_size_on_page of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._emulate_rendering_to_size_on_page

    @emulate_rendering_to_size_on_page.setter
    def emulate_rendering_to_size_on_page(self, emulate_rendering_to_size_on_page):
        """Sets the emulate_rendering_to_size_on_page of this MetafileRenderingOptionsData.

        Gets or sets a value determining whether metafile rendering emulates the display of the metafile according to the size on page or the display of the metafile in its default size.  # noqa: E501

        :param emulate_rendering_to_size_on_page: The emulate_rendering_to_size_on_page of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._emulate_rendering_to_size_on_page = emulate_rendering_to_size_on_page

    @property
    def emulate_rendering_to_size_on_page_resolution(self):
        """Gets the emulate_rendering_to_size_on_page_resolution of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the resolution in pixels per inch for the emulation of metafile rendering to the size on page. This option is used only when EmulateRenderingToSizeOnPage is set to true.The default value is 96. This is a default display resolution. I.e. metafile rendering will emulate the display of the metafile in MS Word with a 100% zoom factor.  # noqa: E501

        :return: The emulate_rendering_to_size_on_page_resolution of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._emulate_rendering_to_size_on_page_resolution

    @emulate_rendering_to_size_on_page_resolution.setter
    def emulate_rendering_to_size_on_page_resolution(self, emulate_rendering_to_size_on_page_resolution):
        """Sets the emulate_rendering_to_size_on_page_resolution of this MetafileRenderingOptionsData.

        Gets or sets the resolution in pixels per inch for the emulation of metafile rendering to the size on page. This option is used only when EmulateRenderingToSizeOnPage is set to true.The default value is 96. This is a default display resolution. I.e. metafile rendering will emulate the display of the metafile in MS Word with a 100% zoom factor.  # noqa: E501

        :param emulate_rendering_to_size_on_page_resolution: The emulate_rendering_to_size_on_page_resolution of this MetafileRenderingOptionsData.  # noqa: E501
        :type: int
        """
        self._emulate_rendering_to_size_on_page_resolution = emulate_rendering_to_size_on_page_resolution

    @property
    def rendering_mode(self):
        """Gets the rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the option that controls how metafile images should be rendered.  # noqa: E501

        :return: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._rendering_mode

    @rendering_mode.setter
    def rendering_mode(self, rendering_mode):
        """Sets the rendering_mode of this MetafileRenderingOptionsData.

        Gets or sets the option that controls how metafile images should be rendered.  # noqa: E501

        :param rendering_mode: The rendering_mode of this MetafileRenderingOptionsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["VectorWithFallback", "Vector", "Bitmap"]  # noqa: E501
        if not rendering_mode.isdigit():
            if rendering_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `rendering_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(rendering_mode, allowed_values))
            self._rendering_mode = rendering_mode
        else:
            self._rendering_mode = allowed_values[int(rendering_mode) if six.PY3 else long(rendering_mode)]

    @property
    def use_emf_embedded_to_wmf(self):
        """Gets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501

        Gets or sets the flag, that controls how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :return: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._use_emf_embedded_to_wmf

    @use_emf_embedded_to_wmf.setter
    def use_emf_embedded_to_wmf(self, use_emf_embedded_to_wmf):
        """Sets the use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.

        Gets or sets the flag, that controls how WMF metafiles with embedded EMF metafiles should be rendered.  # noqa: E501

        :param use_emf_embedded_to_wmf: The use_emf_embedded_to_wmf of this MetafileRenderingOptionsData.  # noqa: E501
        :type: bool
        """
        self._use_emf_embedded_to_wmf = use_emf_embedded_to_wmf


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

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
        if not isinstance(other, MetafileRenderingOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other