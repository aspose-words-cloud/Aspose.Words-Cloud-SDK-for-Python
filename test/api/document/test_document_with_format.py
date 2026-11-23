# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_with_format.py">
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

import os
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to get document with different format.
#
class TestDocumentWithFormat(BaseTestContext):
    #
    # Test for getting document with specified format.
    #
    def test_get_document_with_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/DocumentWithFormat'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentWithFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(name=remote_file_name, format='text', folder=remote_data_folder)

        result = self.words_api.get_document_with_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting document with specified format.
    #
    def test_get_document_with_format_and_out_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/DocumentWithFormat'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentWithFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentWithFormatRequest(name=remote_file_name, format='text', folder=remote_data_folder, out_path=self.remote_test_out + '/TestGetDocumentWithFormatAndOutPath.text')

        result = self.words_api.get_document_with_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')

