# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_table_cell_request.py">
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

class GetTableCellRequest(BaseRequestObject):
    """
    Request model for get_table_cell operation.
    Initializes a new instance.
    :param name The filename of the input document.
    :param table_row_path The path to the table row in the document tree.
    :param index Object index.
    :param folder Original document folder.
    :param storage Original document storage.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password of protected Word document. Use the parameter to pass a password via SDK. SDK encrypts it automatically. We don't recommend to use the parameter to pass a plain password for direct call of API.
    :param encrypted_password Password of protected Word document. Use the parameter to pass an encrypted password for direct calls of API. See SDK code for encyption details.
    :param open_type_support The value indicates whether OpenType support is on.
    """

    def __init__(self, name, table_row_path, index, folder=None, storage=None, load_encoding=None, password=None, encrypted_password=None, open_type_support=None):
        self.name = name
        self.table_row_path = table_row_path
        self.index = index
        self.folder = folder
        self.storage = storage
        self.load_encoding = load_encoding
        self.password = password
        self.encrypted_password = encrypted_password
        self.open_type_support = open_type_support

    def get_original_request(self):
        return self

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_cell`")  # noqa: E501
        # verify the required parameter 'table_row_path' is set
        if self.table_row_path is None:
            raise ValueError("Missing the required parameter `table_row_path` when calling `get_table_cell`")  # noqa: E501
        # verify the required parameter 'index' is set
        if self.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_table_cell`")  # noqa: E501

        path = '/v4.0/words/{name}/{tableRowPath}/cells/{index}'
        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name  # noqa: E501
        else:
            path_params['name'] = ''  # noqa: E501
        if self.table_row_path is not None:
            path_params['tableRowPath'] = self.table_row_path  # noqa: E501
        else:
            path_params['tableRowPath'] = ''  # noqa: E501
        if self.index is not None:
            path_params['index'] = self.index  # noqa: E501
        else:
            path_params['index'] = ''  # noqa: E501

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

        header_params = {}

        file_content_params = []
        form_params = []

        for file_content_value in file_content_params:
            file_content_value.encryptPassword(encryptor)
            if file_content_value.source == 'Request':
                form_params.append([file_content_value.reference, file_content_value.content, 'file'])  # noqa: E501

        return {
            "method": "GET",
            "path": path,
            "body": None,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "collection_formats": collection_formats,
            "response_type": 'TableCellResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'TableCellResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), TableCellResponse)
