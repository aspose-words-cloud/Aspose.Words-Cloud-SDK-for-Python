# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="upload_file_request.py">
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

class UploadFileRequest(BaseRequestObject):
    """
    Request model for upload_file operation.
    Initializes a new instance.
    :param file_content File to upload.
    :param path Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext If the content is multipart and path does not contains the file name it tries to get them from filename parameter from Content-Disposition header.
    :param storage_name Storage name.
    """

    def __init__(self, file_content, path, storage_name=None):
        self.file_content = file_content
        self.path = path
        self.storage_name = storage_name

    def get_original_request(self):
        return self

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'file_content' is set
        if self.file_content is None:
            raise ValueError("Missing the required parameter `file_content` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")  # noqa: E501

        path = '/v4.0/words/storage/file/{path}'
        path_params = {}
        if self.path is not None:
            path_params['path'] = self.path  # noqa: E501
        else:
            path_params['path'] = ''  # noqa: E501

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
        if self.storage_name is not None:
                query_params.append(('storageName', self.storage_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.file_content is not None:
            form_params.append(['fileContent', self.file_content, 'file'])  # noqa: E501

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
            "response_type": 'FilesUploadResult'  # noqa: E501
        }

    def get_response_type(self):
        return 'FilesUploadResult'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), FilesUploadResult)
