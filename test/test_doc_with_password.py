# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_doc_with_password.py">
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

from urllib3 import request
import asposewordscloud.models
import os
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

class TestDocWithPassword(BaseTestContext):
    #
    # Test for getting all paragraphs from protected docx.
    #
    def test_get_document_paragraphs(self):
        remote_data_folder = self.remote_test_folder + '/Common'
        local_file = 'Common/DocWithPassword.docx'
        remote_file_name = 'test_get_document_paragraphs.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder, password='12345')

        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraphs, 'Validate GetDocumentParagraphs response')
        self.assertIsNotNone(result.paragraphs.paragraph_link_list, 'Validate GetDocumentParagraphs response')
        self.assertEqual(2, len(result.paragraphs.paragraph_link_list))