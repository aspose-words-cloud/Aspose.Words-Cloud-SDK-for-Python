# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="split_document_request.py">
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

class SplitDocumentRequest(BaseRequestObject):
    """
    Request model for split_document operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param format The format to split.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password of protected Word document. Use the parameter to pass a password via SDK. SDK encrypts it automatically. We don't recommend to use the parameter to pass a plain password for direct call of API.
    :param encrypted_password Password of protected Word document. Use the parameter to pass an encrypted password for direct calls of API. See SDK code for encyption details.
    :param open_type_support The value indicates whether OpenType support is on.
    :param dest_file_name Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
    :param _from The start page.
    :param to The end page.
    :param zip_output The flag indicating whether to ZIP the output.
    :param fonts_location Folder in filestorage with custom fonts.
    """

    def __init__(self, name, format, folder=None, storage=None, load_encoding=None, password=None, encrypted_password=None, open_type_support=None, dest_file_name=None, _from=None, to=None, zip_output=None, fonts_location=None):
        self.name = name
        self.format = format
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.encrypted_password = encrypted_password
        self.open_type_support = open_type_support
        self.dest_file_name = dest_file_name
        self._from = _from
        self.to = to
        self.zip_output = zip_output
        self.fonts_location = fonts_location

    def get_original_request(self):
        return self

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `split_document`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError("Missing the required parameter `format` when calling `split_document`")  # noqa: E501

        path = '/v4.0/words/{name}/split'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501

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
        if self.format is not None:
                query_params.append(('format', self.format))  # noqa: E501
        if self.folder is not None:
                query_params.append(('folder', self.folder))  # noqa: E501
        if self.storage is not None:
                query_params.append(('storage', self.storage))  # noqa: E501
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.encrypted_password is not None:
                query_params.append(('encryptedPassword', self.encrypted_password))  # noqa: E501
        if self.open_type_support is not None:
                query_params.append(('openTypeSupport', self.open_type_support))  # noqa: E501
        if self.dest_file_name is not None:
                query_params.append(('destFileName', self.dest_file_name))  # noqa: E501
        if self._from is not None:
                query_params.append(('from', self._from))  # noqa: E501
        if self.to is not None:
                query_params.append(('to', self.to))  # noqa: E501
        if self.zip_output is not None:
                query_params.append(('zipOutput', self.zip_output))  # noqa: E501
        if self.fonts_location is not None:
                query_params.append(('fontsLocation', self.fonts_location))  # noqa: E501

        header_params = {}

        file_content_params = []
        form_params = []

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
            "response_type": 'SplitDocumentResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'SplitDocumentResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), SplitDocumentResponse)
