# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="execute_mail_merge_online_job_request.py">
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

class ExecuteMailMergeOnlineJobRequest(BaseRequestObject):
    """
    Request model for execute_mail_merge_online_job operation.
    Initializes a new instance.
    :param template File with template.
    :param data File with mailmerge data.
    :param options Field options.
    :param with_regions The flag indicating whether to execute Mail Merge operation with regions.
    :param merge_whole_document The flag indicating whether fields in whole document are updated while executing of a mail merge with regions.
    :param cleanup The cleanup options.
    :param document_file_name The filename of the output document, that will be used when the resulting document has a dynamic field {filename}. If it is not set, the "template" will be used instead.
    """

    def __init__(self, template, data, options=None, with_regions=None, merge_whole_document=None, cleanup=None, document_file_name=None):
        self.template = template
        self.data = data
        self.options = options
        self.with_regions = with_regions
        self.merge_whole_document = merge_whole_document
        self.cleanup = cleanup
        self.document_file_name = document_file_name

    def get_original_request(self):
        return ExecuteMailMergeOnlineRequest(self.template, self.data, self.options, self.with_regions, self.merge_whole_document, self.cleanup, self.document_file_name)

    def create_http_request(self, api_client, encryptor):
        # verify the required parameter 'template' is set
        if self.template is None:
            raise ValueError("Missing the required parameter `template` when calling `execute_mail_merge_online_job`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.data is None:
            raise ValueError("Missing the required parameter `data` when calling `execute_mail_merge_online_job`")  # noqa: E501
        if self.options is not None:
            self.options.validate()


        path = '/v4.0/words/job/put/MailMerge'
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
        if self.with_regions is not None:
                query_params.append(('withRegions', self.with_regions))  # noqa: E501
        if self.merge_whole_document is not None:
                query_params.append(('mergeWholeDocument', self.merge_whole_document))  # noqa: E501
        if self.cleanup is not None:
                query_params.append(('cleanup', self.cleanup))  # noqa: E501
        if self.document_file_name is not None:
                query_params.append(('documentFileName', self.document_file_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        file_content_params = []
        form_params = []
        if self.template is not None:
            form_params.append(['template', self.template, 'file'])  # noqa: E501
        if self.data is not None:
            form_params.append(['data', self.data, 'file'])  # noqa: E501
        if self.options is not None:
            form_params.append(['options', self.options, 'json'])  # noqa: E501

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
            "response_type": 'JobInfo'  # noqa: E501
        }

    def get_response_type(self):
        return 'JobInfo'  # noqa: E501

    def deserialize_response(self, api_client, response):
        return api_client.deserialize(response.data, response.getheaders(), JobInfo)
