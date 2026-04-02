# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="save_as_tiff_online_request.py">
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
import json

from six.moves.urllib.parse import quote
from asposewordscloud import *
from asposewordscloud.models import *
from asposewordscloud.models.requests import *
from asposewordscloud.models.responses import *

class SaveAsTiffOnlineRequest(BaseRequestObject):
    """
    Request model for save_as_tiff_online operation.
    Initializes a new instance.
    :param document The document.
    :param save_options Tiff save options.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password of protected Word document. Use the parameter to pass a password via SDK. SDK encrypts it automatically. We don't recommend to use the parameter to pass a plain password for direct call of API.
    :param encrypted_password Password of protected Word document. Use the parameter to pass an encrypted password for direct calls of API. See SDK code for encyption details.
    :param open_type_support The value indicates whether OpenType support is on.
    :param use_anti_aliasing The flag indicating whether to use antialiasing.
    :param use_high_quality_rendering The flag indicating whether to use high quality.
    :param image_brightness The level of brightness for the generated images.
    :param image_color_mode The color mode for the generated images.
    :param image_contrast The contrast for the generated images.
    :param numeral_format The images numeral format.
    :param page_count The number of pages to render.
    :param page_index The index of the page to start rendering.
    :param paper_color The background image color.
    :param pixel_format The pixel format of the generated images.
    :param resolution The resolution of the generated images.
    :param scale The zoom factor for the generated images.
    :param tiff_compression The compression tipe.
    :param dml_rendering_mode The optional dml rendering mode. The default value is Fallback.
    :param dml_effects_rendering_mode The optional dml effects rendering mode. The default value is Simplified.
    :param tiff_binarization_method The optional TIFF binarization method. Possible values are: FloydSteinbergDithering, Threshold.
    :param zip_output The flag indicating whether to ZIP the output.
    :param fonts_location Folder in filestorage with custom fonts.
    """

    def __init__(self, document, save_options, load_encoding=None, password=None, encrypted_password=None, open_type_support=None, use_anti_aliasing=None, use_high_quality_rendering=None, image_brightness=None, image_color_mode=None, image_contrast=None, numeral_format=None, page_count=None, page_index=None, paper_color=None, pixel_format=None, resolution=None, scale=None, tiff_compression=None, dml_rendering_mode=None, dml_effects_rendering_mode=None, tiff_binarization_method=None, zip_output=None, fonts_location=None):
        self.document = document
        self.save_options = save_options
        self.load_encoding = load_encoding
        self.password = password
        self.encrypted_password = encrypted_password
        self.open_type_support = open_type_support
        self.use_anti_aliasing = use_anti_aliasing
        self.use_high_quality_rendering = use_high_quality_rendering
        self.image_brightness = image_brightness
        self.image_color_mode = image_color_mode
        self.image_contrast = image_contrast
        self.numeral_format = numeral_format
        self.page_count = page_count
        self.page_index = page_index
        self.paper_color = paper_color
        self.pixel_format = pixel_format
        self.resolution = resolution
        self.scale = scale
        self.tiff_compression = tiff_compression
        self.dml_rendering_mode = dml_rendering_mode
        self.dml_effects_rendering_mode = dml_effects_rendering_mode
        self.tiff_binarization_method = tiff_binarization_method
        self.zip_output = zip_output
        self.fonts_location = fonts_location

    def get_original_request(self):
        return self

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'document' is set
        if self.document is None:
            raise ValueError("Missing the required parameter `document` when calling `save_as_tiff_online`")  # noqa: E501
        # verify the required parameter 'save_options' is set
        if self.save_options is None:
            raise ValueError("Missing the required parameter `save_options` when calling `save_as_tiff_online`")  # noqa: E501
        if self.save_options is not None:
            self.save_options.validate()


        path = '/v4.0/words/online/put/saveAs/tiff'
        path_params = {}

        # path parameters
        collection_formats = {}
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                path = path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=api_client.configuration.safe_chars_for_path_param)
                )

        # remove optional path parameters
        path = path.replace('//', '/')

        query_params = []
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.encrypted_password is not None:
                query_params.append(('encryptedPassword', self.encrypted_password))  # noqa: E501
        if self.open_type_support is not None:
                query_params.append(('openTypeSupport', self.open_type_support))  # noqa: E501
        if self.use_anti_aliasing is not None:
                query_params.append(('useAntiAliasing', self.use_anti_aliasing))  # noqa: E501
        if self.use_high_quality_rendering is not None:
                query_params.append(('useHighQualityRendering', self.use_high_quality_rendering))  # noqa: E501
        if self.image_brightness is not None:
                query_params.append(('imageBrightness', self.image_brightness))  # noqa: E501
        if self.image_color_mode is not None:
                query_params.append(('imageColorMode', self.image_color_mode))  # noqa: E501
        if self.image_contrast is not None:
                query_params.append(('imageContrast', self.image_contrast))  # noqa: E501
        if self.numeral_format is not None:
                query_params.append(('numeralFormat', self.numeral_format))  # noqa: E501
        if self.page_count is not None:
                query_params.append(('pageCount', self.page_count))  # noqa: E501
        if self.page_index is not None:
                query_params.append(('pageIndex', self.page_index))  # noqa: E501
        if self.paper_color is not None:
                query_params.append(('paperColor', self.paper_color))  # noqa: E501
        if self.pixel_format is not None:
                query_params.append(('pixelFormat', self.pixel_format))  # noqa: E501
        if self.resolution is not None:
                query_params.append(('resolution', self.resolution))  # noqa: E501
        if self.scale is not None:
                query_params.append(('scale', self.scale))  # noqa: E501
        if self.tiff_compression is not None:
                query_params.append(('tiffCompression', self.tiff_compression))  # noqa: E501
        if self.dml_rendering_mode is not None:
                query_params.append(('dmlRenderingMode', self.dml_rendering_mode))  # noqa: E501
        if self.dml_effects_rendering_mode is not None:
                query_params.append(('dmlEffectsRenderingMode', self.dml_effects_rendering_mode))  # noqa: E501
        if self.tiff_binarization_method is not None:
                query_params.append(('tiffBinarizationMethod', self.tiff_binarization_method))  # noqa: E501
        if self.zip_output is not None:
                query_params.append(('zipOutput', self.zip_output))  # noqa: E501
        if self.fonts_location is not None:
                query_params.append(('fontsLocation', self.fonts_location))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.document is not None:
            form_params.append(['document', self.document, 'file'])  # noqa: E501
        if self.save_options is not None:
            form_params.append(['saveOptions', self.save_options, 'json'])  # noqa: E501

        for file_content_value in file_content_params:
            file_content_value.encryptPassword(encryptor)
            if file_content_value.source == 'Request':
                form_params.append([file_content_value.reference, file_content_value.content, 'file'])  # noqa: E501

        return {
            "method": "PUT",
            "path": path,
            "body": None,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "collection_formats": collection_formats,
            "response_type": 'SaveAsTiffOnlineResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'SaveAsTiffOnlineResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        multipart = self.getparts(response)
        return SaveAsTiffOnlineResponse(
          api_client.deserialize(api_client.findMultipartByName(multipart, "Model").content, api_client.findMultipartByName(multipart, "Model").headers, SaveResponse),
          api_client.deserialize_files_collection(api_client.findMultipartByName(multipart, "Document").content, api_client.findMultipartByName(multipart, "Document").headers))
