# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="copy_file_request.py">
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

class CopyFileRequest(BaseRequestObject):
    """
    Request model for copy_file operation.
    Initializes a new instance.
    :param dest_path Destination file path.
    :param src_path Source file's path e.g. '/Folder 1/file.ext' or '/Bucket/Folder 1/file.ext'.
    :param src_storage_name Source storage name.
    :param dest_storage_name Destination storage name.
    :param version_id File version ID to copy.
    """

    def __init__(self, dest_path, src_path, src_storage_name=None, dest_storage_name=None, version_id=None):
        self.dest_path = dest_path
        self.src_path = src_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name
        self.version_id = version_id

    def get_original_request(self):
        return self

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")  # noqa: E501
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")  # noqa: E501

        path = '/v4.0/words/storage/file/copy/{srcPath}'
        path_params = {}
        if self.src_path is not None:
            path_params['srcPath'] = self.src_path  # noqa: E501
        else:
            path_params['srcPath'] = ''  # noqa: E501

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
        if self.dest_path is not None:
                query_params.append(('destPath', self.dest_path))  # noqa: E501
        if self.src_storage_name is not None:
                query_params.append(('srcStorageName', self.src_storage_name))  # noqa: E501
        if self.dest_storage_name is not None:
                query_params.append(('destStorageName', self.dest_storage_name))  # noqa: E501
        if self.version_id is not None:
                query_params.append(('versionId', self.version_id))  # noqa: E501

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
            "response_type": 'None'  # noqa: E501
        }

    def get_response_type(self):
        return 'None'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return None
