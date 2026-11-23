# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_compress_document.py">
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
# Example of how to compress document for reduce document size.
#
class TestCompressDocument(BaseTestContext):
    #
    # Test for compression document.
    #
    def test_compress_document(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/CompressDocument'
        local_folder = 'DocumentActions/CompressDocument'
        local_name = 'TestCompress.docx'
        remote_name = 'TestCompress.docx'

        self.upload_file(remote_folder + '/' + remote_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name), 'rb'))

        request_compress_options = asposewordscloud.CompressOptions()
        request = asposewordscloud.models.requests.CompressDocumentRequest(name=remote_name, compress_options=request_compress_options, folder=remote_folder)

        result = self.words_api.compress_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate CompressDocument response')

    #
    # Test for compression document online.
    #
    def test_compress_document_online(self):
        local_folder = 'DocumentActions/CompressDocument'
        local_name = 'TestCompress.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name), 'rb')
        request_compress_options = asposewordscloud.CompressOptions()
        request = asposewordscloud.models.requests.CompressDocumentOnlineRequest(document=request_document, compress_options=request_compress_options)

        result = self.words_api.compress_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

